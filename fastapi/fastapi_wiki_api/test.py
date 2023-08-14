#!/usr/bin/env python3

import unittest

import api
import constants
import tools


class TestAPI_TopPageViews(unittest.TestCase):
    def setUp(self):
        pass

    def test_top_page_views(self):
        # http://127.0.0.1:8000/api/v1/top_page_views
        actual = api.top_page_views()
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], tools.generate_yesterday())
        self.assertEqual(actual["date_end"], tools.generate_yesterday())

        # http://127.0.0.1:8000/api/v1/top_page_views?window=week
        actual = api.top_page_views(window="week")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], tools.generate_days_ago(constants.WINDOW["week"]))
        self.assertEqual(actual["date_end"], tools.generate_yesterday())

        # http://127.0.0.1:8000/api/v1/top_page_views?date_start=2015/10/10&window=week
        actual = api.top_page_views(date_start= "2015/10/10", window="week")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], "2015/10/10")
        self.assertEqual(actual["date_end"], "2015/10/16")
        self.assertEqual(actual["final_results"]["Main_Page"], 132337757)


class TestAPI_ArticleTotalViewPeriod(unittest.TestCase):
    def setUp(self):
        pass

    def test_article_total_view_for_period(self):
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total
        actual = api.article_total_view_for_period(article_name="Albert_Einstein")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], tools.remove_fwd_slash_format(tools.generate_yesterday()))
        self.assertEqual(actual["date_end"], tools.remove_fwd_slash_format(tools.generate_yesterday()))

        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?window=week
        actual = api.article_total_view_for_period(article_name="Albert_Einstein", window="week")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], tools.remove_fwd_slash_format(tools.generate_yesterday()))
        self.assertEqual(actual["date_end"], tools.remove_fwd_slash_format(tools.generate_dates(tools.generate_yesterday(), constants.WINDOW["week"])[-1]))

        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/total?date_start=2015/10/10&date_end=2015/10/12
        actual = api.article_total_view_for_period(article_name="Albert_Einstein", date_start= "2015/10/10", date_end="2015/10/12")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], "20151010")
        self.assertEqual(actual["date_end"], "20151012")
        self.assertEqual(actual["final_results"]["Albert_Einstein"], 55861)
    

class TestAPI_ArticleHighestViewDuringPeriod(unittest.TestCase):
    def setUp(self):
        pass

    def test_article_highest_view_during_period(self):
        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max
        actual = api.article_highest_view_during_period(article_name="Albert_Einstein")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], tools.remove_fwd_slash_format(tools.generate_yesterday()))
        self.assertEqual(actual["date_end"], tools.remove_fwd_slash_format(tools.generate_yesterday()))

        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?window=week
        actual = api.article_highest_view_during_period(article_name="Albert_Einstein", window="week")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], tools.remove_fwd_slash_format(tools.generate_yesterday()))
        self.assertEqual(actual["date_end"], tools.remove_fwd_slash_format(tools.generate_dates(tools.generate_yesterday(), constants.WINDOW["week"])[-1]))

        # http://127.0.0.1:8000/api/v1/article/Albert_Einstein/max?date_start=2015/10/10&date_end=2015/10/12
        actual = api.article_highest_view_during_period(article_name="Albert_Einstein", date_start= "2015/10/10", date_end="2015/10/12")
        self.assertEqual(actual["status"], 200)
        self.assertEqual(actual["date_start"], "20151010")
        self.assertEqual(actual["date_end"], "20151012")
        self.assertEqual(actual["max_views"], 20251)
        self.assertEqual(actual["max_day"], "2015/10/12")


if __name__ == "__main__":
    unittest.main()