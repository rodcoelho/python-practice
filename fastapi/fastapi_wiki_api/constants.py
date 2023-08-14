#!/usr/bin/env python3
HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

TOP_VIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/{date}"
ARTICLE_PAGE_VIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{article_name}/daily/{date_start}00/{date_end}00"

DAY = "day"
WEEK = "week"
MONTH = "month"

WINDOW = {
    DAY: 1,
    WEEK: 7,
    MONTH: 30
}

YYYYMMDD_SLASH = "%Y/%m/%d"

SUCCESS = 200
FAIL = 404