#!/usr/bin/env python

import json

with open("without_china.json") as fd:
    data = json.load(fd)

for i,o in enumerate(data):
    data[i]['active_confirmed_infections']=o['cumultative_confirmed_cases']-o['cumultative_deaths']
    
    if (o['cumultative_confirmed_cases'] > 0) and (o['cumultative_confirmed_cases'] != o['daily_confirmed_cases']):
        data[i]['rate_cases'] = o['daily_confirmed_cases']/o['cumultative_confirmed_cases']
        data[i]['change_rate_cases'] = o['daily_confirmed_cases']/(o['cumultative_confirmed_cases']-o['daily_confirmed_cases'])
        data[i]['rate_mortality'] = o['cumultative_deaths']/o['cumultative_confirmed_cases']
    else:
        data[i]['rate_cases']=0.0
        data[i]['change_rate_cases']=0.0
        
    if (o['cumultative_deaths'] > 0) and (o['cumultative_deaths'] != o['daily_deaths']):
        data[i]['change_rate_deaths'] = o['daily_deaths']/(o['cumultative_deaths']-o['daily_deaths'])
        data[i]['rate_deaths'] = o['daily_deaths']/o['cumultative_deaths']
    else:
        data[i]['rate_deaths']=0.0
        data[i]['change_rate_deaths']=0.0

with open("foobar.json","w") as fd:
    json.dump(data,fd)
