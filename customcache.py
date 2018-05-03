#!/usr/bin/env python3

import time                                 # import for getting unix time
import datetime                             # import for getting time
from random import randint                  # import for generating fake database queries


class TTDCache:
    def __init__(self, n):
        self.cache = {}                     # the cache
        self.cache_size = n                 # the cache's maximum capacity
        self.replacement_algo = 'LRU'       # the cache's replacement method for maintaining capacity

    def __contains__(self, key):            # allows us to do something like: if x in object
        return key in self.cache            # returns True or False

    def get(self, key):
        # if key is in cache, return value
        if key in self.cache:
            value = self.cache[key]['value']
            self.cache[key]['unix'] = time.time()                               # update unix time of query
            self.cache[key]['conventional_time'] = datetime.datetime.now()      # update time of query
            self.cache[key]['count'] += 1                                       # increase counter for num of queries
            return value

        # if key not in cache, get from database and save to cache
        else:
            # query database
            value = self.query_database(key)

            # check if cache is at capacity
            if len(self.cache) >= self.cache_size:
                # if at capacity, then call replacement algo function
                self.algo()

            # store key/value in cache for future use
            self.cache[key] = {
                'value': value,
                'unix': time.time(),
                'conventional_time': datetime.datetime.now(),
                'count': 1
            }
            return self.cache[key]['value']

    def query_database(self, key):
        # fake database query
        # should be replaced with a real query to a database
        value = str(randint(0, 10000)) + str(key)
        return value

    def algo(self):
        # if LRU, pop the oldest
        if self.replacement_algo == 'LRU':
            oldest = None
            for key in self.cache:
                if oldest is None:
                    if key is not None:
                        oldest = key
                    else:
                        pass
                        # FIXME edge case for if key == None
                elif self.cache[key]['conventional_time'] < self.cache[oldest]['conventional_time']:
                    oldest = key
            self.cache.pop(oldest)

        # if MRU, pop the newest
        elif self.replacement_algo == 'MRU':
            newest = None
            for key in self.cache:
                if newest is None:
                    if key is not None:
                        newest = key
                    else:
                        pass
                        # FIXME edge case for if key == None
                elif self.cache[key]['conventional_time'] > self.cache[newest]['conventional_time']:
                    newest = key
            self.cache.pop(newest)

    def clear_cache(self):
        # clear cache is important if the database is altered and we can't trust the cache anymore
        self.cache = {}

