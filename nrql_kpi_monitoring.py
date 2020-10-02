#!/usr/local/bin/python3

from nrql.api import NRQL
from pandas import DataFrame
import getpass
import datetime

nrql = NRQL()
nrql.api_key = 'x***************************'
nrql.account_id = '16****66'

username = getpass.getuser()

since = ' SINCE 12 hours ago'

l1 = ['SiteServer', 'buildyourbet', 'opta-scoreboards', 'surface-bets', 'stats-centre']
l2 = []
l3 = []
l4 = []

queries = ["SELECT average(time/1000) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE 'https://ss-aka-ori%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'LB-SPT-OXYGEN-VNL-PRD0' AND time<60000", "SELECT average(time/1000) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE '%buildyourbet%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'LB-SPT-OXYGEN-VNL-PRD0' AND time<60000", "SELECT average(time/1000) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE '%opta-scoreboards%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'LB-SPT-OXYGEN-VNL-PRD0' AND time<60000", "SELECT average(time/1000) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE '%surface-bets%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'LB-SPT-OXYGEN-VNL-PRD0' AND time<60000", "SELECT average(time/1000) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE '%stats-centre%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'LB-SPT-OXYGEN-VNL-PRD0' AND time<60000", "SELECT count(*) as 'Requests' FROM PageAction where actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' and url LIKE '%ss-aka-ori%'", "SELECT count(*) as 'Requests' FROM PageAction where actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' and url LIKE '%buildyourbet%'", "SELECT count(*) as 'Requests' FROM PageAction where actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' and url LIKE '%opta-scoreboards%'", "SELECT count(*) as 'Requests' FROM PageAction where actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' and url LIKE '%surface-bets%'", "SELECT count(*) as 'Requests' FROM PageAction where actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' and url LIKE '%stats-centre%'", "SELECT filter(count(*), WHERE url LIKE '%ss-aka-ori%' AND status NOT IN (200)) * 100 / filter(count(*), WHERE url LIKE '%ss-aka-ori%') as 'ss-aka-ori error rate' from PageAction WHERE actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' EXTRAPOLATE ", "SELECT filter(count(*), WHERE url LIKE '%buildyourbet%' AND status NOT IN (200)) * 100 / filter(count(*), WHERE url LIKE '%buildyourbet%') as 'buildyourbet error rate' from PageAction WHERE actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' EXTRAPOLATE ", "SELECT filter(count(*), WHERE url LIKE '%opta-scoreboards%' AND status NOT IN (200)) * 100 / filter(count(*), WHERE url LIKE '%opta-scoreboards%') as 'opta-scoreboards error rate' from PageAction WHERE actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' EXTRAPOLATE ", "SELECT filter(count(*), WHERE url LIKE '%surface-bets%' AND status NOT IN (200)) * 100 / filter(count(*), WHERE url LIKE '%surface-bets%') as 'surface-bets error rate' from PageAction WHERE actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' EXTRAPOLATE ", "SELECT filter(count(*), WHERE url LIKE '%stats-centre%' AND status NOT IN (200)) * 100 / filter(count(*), WHERE url LIKE '%stats-centre%') as 'stats-centre error rate' from PageAction WHERE actionName = 'Ajax Call' and appName = 'LB-SPT-OXYGEN-VNL-PRD0' EXTRAPOLATE"]

for i in queries:
    result = nrql.query(i + since)
    for a in result['results']:
        try:
            l2.append(round(a['average'], 3))
        except KeyError as err:
            try:
                l3.append(a['count'])
            except:
                l4.append(round(a['result'], 3))


for n, i in enumerate(l4):
    if i == 0:
        l4[n] = '< 0,001'
    elif i == None:
        l4[n] = "N/A"
for n, i in enumerate(l2):
    if i == None:
        l2[n] = "N/A"
try:
    df = DataFrame({'Metric name': l1, 'Response time': l2, 'Request count': l3, 'Error Rate': l4})
    df.to_excel(excel_writer = "/Users/" + username + "/Desktop/%s-report.xls" % datetime.datetime.now(), sheet_name='report', index=False)
    print('Check your directory. Report should be ready')
except:
    print ('Contact Yan. There is something wrong with reports generating')