import os
import json
import sys
import requests
import datetime
import csv
from elasticsearch import Elasticsearch
import numpy as np

def clrHidden(input):
    if "\xef\xbb\xbf" in input:
        input = input[3:]
    return input

es = Elasticsearch([{'host': 'localhost', 'port': '9000'}])
es.indices.delete(index='arrivals', ignore=[400, 404])

for file in os.listdir("arrival"):
    with open("arrival/" + file) as dataset:
        lastvalue = None
        arrivaltimes = []
        rdr = csv.reader(dataset, delimiter=' ', quotechar='|')

        for row in rdr:
            if row[0] != "\xef\xbb\xbf":
                line = "".join(row)
                values = line.strip().split(":")
                timevalue = datetime.time(hour=int(clrHidden(values[0])), minute=int(clrHidden(values[1])), second=int(clrHidden(values[2])))
                timestamp = datetime.datetime.combine(datetime.date.today(), timevalue)

                if lastvalue is None:
                    lastvalue = timestamp
                else:
                      difference = timestamp - lastvalue
                      lastvalue = timestamp
                      arrivaltimes.append(round(difference.total_seconds() / 60.0, 2))
    
        dataset_report = {}
        # get mean, median, standard deviation, min and max
        dataset_report['mean'] = round(np.mean(arrivaltimes),2)
        dataset_report['median'] = round(np.median(arrivaltimes),2)
        dataset_report['standard_deviation'] = round(np.std(arrivaltimes),2)
        dataset_report['min'] = round(np.amin(arrivaltimes),2)
        dataset_report['max'] = round(np.amax(arrivaltimes),2)
        dataset_report['data'] = arrivaltimes
        dataset_report['source'] = file

        # For CSV
        #print(str(dataset_report['mean']) + ',' + str(dataset_report['median']) + ',' + str(dataset_report['standard_deviation']) + ',' + str(dataset_report['min']) + ',' + str(dataset_report['max'])+ ',' + file)
        # For Console perusal
        #print('mean:' +str(dataset_report['mean']) + ' \tmed:' + str(dataset_report['median']) + ' \tstd:' + str(dataset_report['standard_deviation']) + ' \tmin:' + str(dataset_report['min']) + ' \tmax:' + str(dataset_report['max'])+ ' \tsrc:' + file)
        es.index(index='arrivals', body=dataset_report)
                  
