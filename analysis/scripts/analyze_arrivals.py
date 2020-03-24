import os
import json
import sys
import requests
from datetime import datetime, time
import csv
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': '9000'}])

for file in os.listdir("arrival"):
    with open("arrival/" + file) as dataset:
        print("processing: " + file)

        lastvalue = None
        arrivaltimes = []
        rdr = csv.reader(dataset, delimiter=' ', quotechar='|')

        for row in rdr:
            if row[0] == "\xef\xbb\xbf":
                print('skip line')
            else:
                line = "".join(row)
                values = line.strip().split(":")
                timestamp = datetime.time(
                    hour=int(
                        values[0]), minute=int(
                        values[1]), second=int(
                        values[2]))

                if lastvalue is None:
                    lastvalue = timestamp
                else:
                      difference = timestamp - lastvalue
                      lastvalue = timestamp
                      print(difference)
                  
