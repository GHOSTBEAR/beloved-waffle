# -*- coding: utf-8 -*-
import argparse
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
    
current = datetime.datetime.now()

parser = argparse.ArgumentParser()

parser.add_argument('-g', "--genre", 
                    help="Filter by genre (default: all)", 
                    default='all')
parser.add_argument('-l', "--limit", 
                    help="Limit amount of shows displayed (default: 10, max: 20)", 
                    default=10)
parser.add_argument('-y', "--year", 
                    help="Filter by year (default: 1907..%d, format: from..to)" % current.year, 
                    default='1907..%d' % current.year)
parser.add_argument('-s', "--sort", 
                    help="Filter by most popular/highest rated (default: popular)", 
                    default='popular')

args = parser.parse_args()

category = args.genre

limit = args.limit

year =  args.year

sort = '-userCount' if args.sort == 'popular' else '-averageRating'

print 'Top %s %s\'s between %s' % (limit, category.capitalize(), year.replace('..', ' to '))

if category != 'all':
    options = {'page[limit]': limit, 'page[offset]': 0, 'filter[genres]': category, 'filter[year]': year, 'sort': sort}
    res = get(URL, options)
else:
    options = {'page[limit]': limit, 'page[offset]': 0, 'filter[year]': year, 'sort': sort}
    res = get(URL, options)

try:
    for position, item in enumerate(res['data'], start=1):
        print '%d: %s, number of user %d average rating %s' % (
            position,
            item['attributes']['canonicalTitle'], 
            item['attributes']['userCount'],
            item['attributes']['averageRating']
        )
        print
except:
    print res['errors'][0]['detail']
