#!/usr/bin/env python

from nrql.api import NRQL
import requests

nrql = NRQL()
nrql.api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
nrql.account_id = '1641266'
rest_api = 'xxxxxxxxxxxxxxxxxx'
arr2 = []
arr3 = []

#executing all opened violations
req1 = nrql.query("SELECT * FROM AlertViolationsSample WHERE policy_name LIKE '%_%Lviv%' and policy_name not LIKE '%hlv%' and priority IN ('Critical', 'Warning') SINCE 1593039600 UNTIL 1593046800 LIMIT MAX")
for i in req1['results']:
    arr1 = i['events']
#executing all events from Ec2Instance provider with 'Agent disconnected' status
req2 = nrql.query("SELECT * FROM InfrastructureEvent WHERE provider = 'Ec2Instance' and summary = 'Agent disconnected' AND hostname NOT LIKE '%hlv%' AND hostname NOT LIKE '%tst%' AND hostname NOT LIKE '%jenkins%' AND hostname NOT LIKE '%stg0%' SINCE 1593028800 UNTIL 1593046800 LIMIT MAX")
for i in req2['results']:
    for a in i['events']:
        arr2.append(a['hostname'])
for i in arr2:
    for a in arr1:
            if i == a['entity.name']: #matching identic hostnames in 2 queries
                arr3.append(a['id'])
arr3 = list(set(arr3)) #violations IDs
for x in arr3: #closing part
    url = "https://api.newrelic.com/v2/alerts_violations/%s/close.json" % x
    print(url)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': '%s' % rest_api
    }
    response = requests.request("PUT", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))