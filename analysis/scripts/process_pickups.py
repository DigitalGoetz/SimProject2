import json
from elasticsearch import Elasticsearch
import numpy as np


es = Elasticsearch([{'host': 'localhost', 'port': '9000'}])
search = es.search(index='pickups', size=5000)
hitarray = search['hits']['hits']

dataset = []
for hit in hitarray:
    data = hit["_source"]["data"]
    for datum in data:
        dataset.append(datum)

dataset_report = {}
# get mean, median, standard deviation, min and max
dataset_report['mean'] = round(np.mean(dataset),2)
dataset_report['median'] = round(np.median(dataset),2)
dataset_report['standard_deviation'] = round(np.std(dataset),2)
dataset_report['min'] = round(np.amin(dataset),2)
dataset_report['max'] = round(np.amax(dataset),2)
dataset.sort()
dataset_report['data'] = dataset

import utils
utils.plot(dataset, 45, 'Pickups')

#print(json.dumps(dataset_report))