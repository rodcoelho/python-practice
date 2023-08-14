#!/usr/bin/env python3
from fastapi import FastAPI, Path, HTTPException, status
from fastapi.responses import RedirectResponse
import requests

from typing import Optional
from collections import Counter

import constants
import tools

app = FastAPI()


# http://127.0.0.1:8000/api/v1/top_page_views
# http://127.0.0.1:8000/api/v1/top_page_views?window=week
# http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&window=week
# http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&date_end=2015/10/13
# http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&date_end=2015/10/13&window=week
@app.get("/api/v1/top_page_views")
def top_page_views(date_start: Optional[str]=None, date_end: Optional[str]=None, window: Optional[str]=constants.DAY):
    ctx = tools.Context(
        date_start=date_start,
        date_end=date_end,
        window=window,
        )
    err = ctx.validate()
    if err:
        return tools.kwargs_to_dict(status=constants.FAIL, error=err)
    
    err = ctx.normalize_top_views_dates()
    if err:
        return tools.kwargs_to_dict(status=constants.FAIL, error=err)

    final_results = Counter()
    for date in ctx.dates:
        try:
            r = requests.get(constants.TOP_VIEWS_URL.format(date=date), headers=constants.HEADERS)
            r.raise_for_status()
            articles = r.json()["items"][0]["articles"]
        except Exception as e:
            return tools.kwargs_to_dict(status=constants.FAIL, error="error retreiving URL")

        for article in articles:
            article_name, article_views = article["article"], article["views"]

            if article_name in final_results:
                final_results[article_name] += article_views
            else:
                final_results[article_name] = article_views

    return tools.kwargs_to_dict(status=constants.SUCCESS, date_start=ctx.date_start, date_end=ctx.dates[-1], final_results=final_results)


# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?window=week
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&window=week
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&date_end=2015/10/12
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&date_end=2015/10/12&window=week
@app.get("/api/v1/article/{article_name}/total")
def article_total_view_for_period(article_name:str, date_start: Optional[str]=None, date_end: Optional[str]=None, window: Optional[str]=constants.DAY):
    ctx = tools.Context(
        date_start=date_start,
        date_end=date_end,
        window=window.lower(),
        article_name=article_name
        )
    err = ctx.validate()
    if err:
        return tools.kwargs_to_dict(status=constants.FAIL, error=err)
    
    err = ctx.normalize_article_dates()
    if err:
        return tools.kwargs_to_dict(status=constants.FAIL, error=err)
    
    try:
        r = requests.get(constants.ARTICLE_PAGE_VIEWS_URL.format(article_name=ctx.article_name, date_start=ctx.date_start, date_end=ctx.date_end), headers=constants.HEADERS)
        r.raise_for_status()
        articles = r.json()["items"]
    except Exception as e:
        return tools.kwargs_to_dict(status=constants.FAIL, error="error retreiving URL")

    final_results = Counter()
    for article in articles:
        article_name, article_views = article["article"], article["views"]

        if article_name in final_results:
            final_results[article_name] += article_views
        else:
            final_results[article_name] = article_views

    return tools.kwargs_to_dict(status=constants.SUCCESS, final_results=final_results, article=ctx.article_name, date_start=ctx.date_start, date_end=ctx.date_end)


# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?window=week
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&window=week
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&date_end=2015/10/12
# http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&date_end=2015/10/12&window=week
@app.get("/api/v1/article/{article_name}/max")
def article_highest_view_during_period(article_name:str, date_start: Optional[str]=None, date_end: Optional[str]=None, window: Optional[str]=constants.DAY):
    ctx = tools.Context(
        date_start=date_start,
        date_end=date_end,
        window=window.lower(),
        article_name=article_name,
        )
    err = ctx.validate()
    if err:
        return tools.kwargs_to_dict(status=constants.FAIL, error=err)
    
    err = ctx.normalize_article_dates()
    if err:
        return tools.kwargs_to_dict(status=constants.FAIL, error=err)
    
    try:
        r = requests.get(constants.ARTICLE_PAGE_VIEWS_URL.format(article_name=ctx.article_name, date_start=ctx.date_start, date_end=ctx.date_end), headers=constants.HEADERS)
        r.raise_for_status()
        articles = r.json()["items"]
    except Exception as e:
        return tools.kwargs_to_dict(status=constants.FAIL, error="error retreiving URL")

    max_views = 0
    max_day = None
    for article in articles:
        article_name, article_views = article["article"], article["views"]

        if article_views > max_views:
            max_views = article_views
            max_day = tools.add_fwd_slash_format(article["timestamp"][:-2])

    return tools.kwargs_to_dict(status=constants.SUCCESS, max_views=max_views, max_day=max_day, article=ctx.article_name, date_start=ctx.date_start, date_end=ctx.date_end)
