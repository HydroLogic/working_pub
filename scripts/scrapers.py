#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, json, sys, string, io
import pandas as pd
import numpy as np
import urllib2
import pycountry

def iso3dict():
    cc_dict = {}
    t = list(pycountry.countries)
    for country in t:
        cc_dict[country.alpha3]=country.name
    return cc_dict

def complete_emdat2df(countryiso, complete_dict):
    complete_dict.setdefault(countryiso, [])
    url='http://www.emdat.be/disaster_list/php/search.php?_dc=1455563990858&continent=&region=&iso='+countryiso+'&from=1800&to=2015&group=Climatological%27%2C%27Geophysical%27%2C%27Hydrological%27%2C%27Meteorological%27%2C%27Complex%20Disasters%27%2C%27Biological%27%2C%27Extra_terrestrial%27%2C%27Technological&type=&options=associated_dis%2Cassociated_dis2%2Ctotal_deaths%2Ctotal_affected%2Ctotal_dam%2Cinsur_dam&page=1&start=0&limit=25'
    response = urllib2.urlopen(url)
    data = json.load(response)
    output = {}
    count = int (len(data['data']) - 1)
    while count >= 0:
        adisaster = data['data'][count]['disaster_no']
        dis_type = data['data'][count]['dis_type']
        dis_subtype = data['data'][count]['dis_subtype']
        st_date = data['data'][count]['start_date']
        end_date = data['data'][count]['end_date']
        iso = data['data'][count]['iso']
        location = data['data'][count]['location']
        total_affected = data['data'][count]['total_affected']
        total_dam = data['data'][count]['total_dam']
        total_deaths = data['data'][count]['total_deaths']
        insur_dam = data['data'][count]['insur_dam']
        adis = {
            "iso": iso,
            "location": location,
            "dis_type": dis_type,
            "dis_subtype": dis_subtype,
            "st_date": st_date,
            "end_date": end_date,
            "total_affected": total_affected,
            "total_dam": total_dam,
            "total_deaths": total_deaths,
            "insur_dam": insur_dam
        }
        output[adisaster] = adis
        count = count - 1
    complete_dict[countryiso] = output
    df = pd.DataFrame.from_dict(output).T
    return df


def nat_disaster_emdat2df(countryiso, complete_dict):
    complete_dict.setdefault(countryiso, [])
    url='http://www.emdat.be/disaster_list/php/search.php?_dc=1455563990858&continent=&region=&iso='+countryiso+'&from=1900&to=2015&group=Climatological%27%2C%27Geophysical%27%2C%27Hydrological%27%2C%27Meteorological&type=&options=associated_dis%2Cassociated_dis2%2Ctotal_deaths%2Ctotal_affected%2Ctotal_dam%2Cinsur_dam&page=1&start=0&limit=25'
    response = urllib2.urlopen(url)
    data = json.load(response)
    output = {}
    count = int (len(data['data']) - 1)
    while count >= 0:
        adisaster = data['data'][count]['disaster_no']
        dis_type = data['data'][count]['dis_type']
        dis_subtype = data['data'][count]['dis_subtype']
        st_date = data['data'][count]['start_date']
        end_date = data['data'][count]['end_date']
        iso = data['data'][count]['iso']
        location = data['data'][count]['location']
        total_affected = data['data'][count]['total_affected']
        total_dam = data['data'][count]['total_dam']
        total_deaths = data['data'][count]['total_deaths']
        insur_dam = data['data'][count]['insur_dam']
        adis = {
            "iso": iso,
            "location": location,
            "dis_type": dis_type,
            "dis_subtype": dis_subtype,
            "st_date": st_date,
            "end_date": end_date,
            "total_affected": total_affected,
            "total_dam": total_dam,
            "total_deaths": total_deaths,
            "insur_dam": insur_dam
        }
        output[adisaster] = adis
        count = count - 1
    complete_dict[countryiso] = output
    df = pd.DataFrame.from_dict(output).T
    return df