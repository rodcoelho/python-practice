# Grow Therapy Coding Challenge

To install packages: 

    pip install -r requirements.txt

To run API

    uvicorn api:app --reload
    # then use one of the endpoints below

To run tests

    python3 test.py


API endpoints

    /api/v1/top_page_views
    "get the most viewed articles for a period and view count"

        args:
            date_start = YYYY/MM/DD
            date_end = YYYY/MM/DD
            window = ONEOF day week month

        examples:
        # http://127.0.0.1:8000/api/v1/top_page_views
        # http://127.0.0.1:8000/api/v1/top_page_views?window=week
        # http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&window=week
        # http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&date_end=2015/10/13
        # http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&date_end=2015/10/13&window=week


    /api/v1/article/{article_name}/total
    "get an article's highest view count day in a given period"

        args:
            article_name = name of article
            date_start = YYYY/MM/DD
            date_end = YYYY/MM/DD
            window = ONEOF day week month (ignored if date_end exists)

        examples:
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?window=week
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&window=week
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&date_end=2015/10/12
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&date_end=2015/10/12&window=week
    

    /api/v1/article/{article_name}/max
    "get an article's day with the max view and the view count in a given period"
        args:
            article_name = name of article
            date_start = YYYY/MM/DD
            date_end = YYYY/MM/DD
            window = ONEOF day week month (ignored if date_end exists)

        examples
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?window=week
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&window=week
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&date_end=2015/10/12
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&date_end=2015/10/12&window=week

