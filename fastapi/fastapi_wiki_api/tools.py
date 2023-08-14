#!/usr/bin/env python3
from datetime import datetime, timedelta

import constants


class Context:
    def __init__(self, date_start:str=None, date_end:str=None, window:str=None, article_name:str=None):
        self.date_start=date_start
        self.date_end=date_end
        self.window=window.lower()
        self.article_name=article_name
        self.dates=[]

    def validate(self):
        if not self.valid_window():
            return "Window not valid"
        if self.date_start:
            if date_is_future(self.date_start):
                return "Date is in future"
        if self.date_end:
            if date_is_future(self.date_end):
                return "Date is in future"
        
    def revalidate(self):
        self.validate()
    
    def valid_window(self):
        return self.window in constants.WINDOW
    
    def normalize_top_views_dates(self):
        if self.date_start and self.date_end:
            # use start and end to make dates
            self.dates = generate_dates_between(self.date_start, self.date_end)
        elif self.window and not self.date_start:
            # use window to create missing start dates
            self.date_start = generate_days_ago(constants.WINDOW[self.window])
            self.dates = generate_dates(self.date_start, constants.WINDOW[self.window])
        elif self.window and self.date_start:
            # use window and start to make dates
            self.dates = generate_dates(self.date_start, constants.WINDOW[self.window])  
        self.revalidate()

    def normalize_article_dates(self):
        if self.date_start and self.date_end:
            # we have everything we need to make URL
            pass
        elif self.date_start and not self.date_end:
            # create date_end with start and window
            self.dates = generate_dates(self.date_start, constants.WINDOW[self.window])
            self.date_end = self.dates[-1]
        elif not self.date_start and not self.date_end:
            # create date_start and date_end using window and yesterday as start
            self.date_start = generate_yesterday()
            self.dates = generate_dates(self.date_start, constants.WINDOW[self.window])
            self.date_end = self.dates[-1]
        self.revalidate()
        
        self.date_start, self.date_end = remove_fwd_slash_format(self.date_start), remove_fwd_slash_format(self.date_end)


def generate_dates(date_str: str, num_of_days: int):
    start_date = datetime.strptime(date_str, constants.YYYYMMDD_SLASH)
    date_list = [(start_date + timedelta(days=i)).strftime(constants.YYYYMMDD_SLASH) for i in range(num_of_days)]
    return date_list

def generate_dates_between(date_start: str, date_end: str):
    date_start, date_end = datetime.strptime(date_start, constants.YYYYMMDD_SLASH), datetime.strptime(date_end, constants.YYYYMMDD_SLASH)
    date_list = []
    current_date = date_start
    while current_date <= date_end:
        date_list.append(current_date.strftime(constants.YYYYMMDD_SLASH))
        current_date += timedelta(days=1)
    return date_list

def generate_today():
    return datetime.now().strftime(constants.YYYYMMDD_SLASH)

def generate_days_ago(num_of_days: int):
    yesterday = datetime.now() - timedelta(days=num_of_days)
    return yesterday.strftime(constants.YYYYMMDD_SLASH)

def generate_yesterday():
    return generate_days_ago(1)

def date_is_future(date_string:str):
    input_date = datetime.strptime(date_string, "%Y/%m/%d")
    current_date = datetime.now()
    return input_date > current_date

def add_fwd_slash_format(date_str: str):
    if '/' not in date_str:
        return date_str[:4] + "/" + date_str[4:6] + "/" + date_str[6:]
    return date_str

def remove_fwd_slash_format(date_str: str):
    if '/' in date_str:
        return date_str.replace("/", "")
    return date_str

def kwargs_to_dict(*args, **kwargs):
    d = {}
    d.update(kwargs)
    return d