import os
import json
import sys
import requests
import datetime
import csv
from elasticsearch import Elasticsearch
import numpy as np


es = Elasticsearch([{'host': 'localhost', 'port': '9000'}])
es.indices.delete(index='pickups', ignore=[400, 404])

def clrHidden(input):
    if "\xef\xbb\xbf" in input:
        input = input[3:]
    return input


for file in os.listdir("pickup"):
    with open("pickup/" + file) as dataset:
        pickuptimes = []
        rdr = csv.reader(dataset, delimiter=' ', quotechar='|')

        for row in rdr:
            line = "".join(row)
            times = line.split(",")
            start = times[0].strip().split(":")
            end = times[1].strip().split(":")
            startvalue = datetime.time(hour=int(clrHidden(start[0])), minute=int(clrHidden(start[1])), second=int(clrHidden(start[2])))
            starttime = datetime.datetime.combine(datetime.date.today(), startvalue)
            endvalue = datetime.time(hour=int(clrHidden(end[0])), minute=int(clrHidden(end[1])), second=int(clrHidden(end[2])))
            endtime = datetime.datetime.combine(datetime.date.today(), endvalue)

            difference = endtime - starttime
            pickuptimes.append(round(difference.total_seconds() / 60.0, 2))
    
        dataset_report = {}
        # get mean, median, standard deviation, min and max
        dataset_report['mean'] = round(np.mean(pickuptimes),2)
        dataset_report['median'] = round(np.median(pickuptimes),2)
        dataset_report['standard_deviation'] = round(np.std(pickuptimes),2)
        dataset_report['min'] = round(np.amin(pickuptimes),2)
        dataset_report['max'] = round(np.amax(pickuptimes),2)
        dataset_report['data'] = pickuptimes
        dataset_report['source'] = file

        # For CSV
        print(str(dataset_report['mean']) + ',' + str(dataset_report['median']) + ',' + str(dataset_report['standard_deviation']) + ',' + str(dataset_report['min']) + ',' + str(dataset_report['max'])+ ',' + file)
        # For Console perusal
        #print('mean:' +str(dataset_report['mean']) + ' \tmed:' + str(dataset_report['median']) + ' \tstd:' + str(dataset_report['standard_deviation']) + ' \tmin:' + str(dataset_report['min']) + ' \tmax:' + str(dataset_report['max'])+ ' \tsrc:' + file)
        es.index(index='pickups', body=dataset_report)
                  
