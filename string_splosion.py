#!/usr/bin/env python3

# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


def string_splosion(str):
    s = str[0]
    for i in range(1,len(str)):
        s += str[:i+1]
    return s

