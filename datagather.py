import pandas as pd
import numpy as np
import requests
import json
import time
from bs4 import BeautifulSoup

def yelp_data(search_term, zipcode, limit, url, api_key):
    '''Pulls data from the yelp API given a search term or terms, zipcode,
       number of queries, the API url and key and returns it as a pandas 
       DataFrame'''
    headers = {'Authorization': 'Bearer {}'.format(api_key),}

    url_params = {
                'term': search_term.replace(' ', '+'),
                'location': 'New York, NY, {zipcode}',
                'limit': limit}
    a = requests.get(url, headers = headers, params= url_params)
    b = a.text
    df = json.loads(b)
    return pd.DataFrame(df['businesses'])

def yelp_dataframe(search_term, list_of_zipcodes, limit, url, api_key):
    """Given a list of zipcodes, pulls data from the yelp API given a search 
       term or terms, number of queries, the API url and key and returns 
       it as an aggregated pandas DataFrame from each zip"""
    main = []
    maindf = pd.DataFrame()
    for i in range(0, len(list_of_zipcodes)):
        main.append(yelp_data(search_term, i, limit, url, api_key))
    for i in main:
        maindf = pd.concat([i, maindf], axis = 0)
    return maindf

def closed_dataframe(list_of_restaurants, list_of_zipcodes, url, api_key):
    """A tool for finding closed restaurants with the yelp API- given an
       exact match of restaurant names in a list and their corresponding 
       zipcodes, the API url and key, returns a DataFrame made up of those
       restaurants' details"""
    ylist = []
    gdataframe = pd.DataFrame()
    for i in range(0, len(list_of_restaurants)):
        ylist.append(yelp_data(list_of_restaurants[i], list_of_zipcodes[i],             1, url, api_key))
    for i in ylist:
        gdataframe = pd.concat([i, gdataframe], axis = 0)
    return gdataframe

def get_features(url):
    """A webscraping tool for pulling special features from a yelp page
       given the url"""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    l = soup.find_all(class_= "lemon--span__373c0__3997G text__373c0__2Kxyz text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B")
    v = []
    for i in l:
        v.append(i.text.strip())
    return v

def outdoor_seating(array_of_lists):
    """Takes the output from get_features and produces a dummy variable
       determined by outdoor seating at the given restaurant"""
    r = []
    for i in array_of_lists:
        if 'Outdoor seating' in i:
            r.append(1)
        else:
            r.append(0)
    return r

def outdoor_seating_column(alias_column):
    """Using outdoor_seating and get_features as helper functions, this takes
       a column of restaurant names and produces a dummy column for outside
       seating"""
    w = []
    for i in list(alias_column):
        url = f'https://www.yelp.com/biz/{i}'
        w.append(get_features(url))
    return outdoor_seating(w)