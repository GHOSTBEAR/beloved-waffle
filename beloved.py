# -*- coding: utf-8 -*-
# from sys import argv
import requests
import datetime
import json

URL = 'http://kitsu.io/api/edge/anime'

def get(url, payload):
    response = requests.get(url, params=payload)
    try:
        return response.json()
    except Exception as e:
        print response
        raise e

def question(array, fallback):
    for item in array:
        print item
    
    return raw_input('>>> ') or fallback

description = [
    '-- Genre --',
    'Default: all',
]
category = question(description , 'all')
print

description = [
    '-- Limit --',
    'Default: 10'
]
limit = question(description , 10)
print

current = datetime.datetime.now()
description = [
    '-- Year --',
    'Format: from..to',
    'Default: 1907..%d' % current.year,
    'Exampel: 2010..2016'
]
year =  question(description , '1907..%d' % current.year)
print

description = [
    '-- Sort By --',
    'Default: -userCount',
    'Alternative: -averageRating'
]
sort =  question(description , '-userCount')
print

print 'Top %s %s\'s between %s' % (limit, category.capitalize(), year.replace('..', ' to '))

if category != 'all':
    options = {'page[limit]': limit, 'page[offset]': 0, 'filter[genres]': category, 'filter[year]': year, 'sort': sort}
    res = get(URL, options)
else:
    options = {'page[limit]': limit, 'page[offset]': 0, 'filter[year]': year, 'sort': sort}
    res = get(URL, options)

for position, item in enumerate(res['data'], start=1):
    print '%d: %s, number of user %d average rating %s' % (
        position,
        item['attributes']['canonicalTitle'], 
        item['attributes']['userCount'],
        item['attributes']['averageRating']
    )
    print
