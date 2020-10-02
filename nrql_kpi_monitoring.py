#!/usr/bin/env python

from nrql.api import NRQL
from pandas import DataFrame
import datetime

nrql = NRQL()
nrql.api_key = 'xAUTO*******-**************-BZFj'
nrql.account_id = '16****6'

print ('====================================')
print ("Response time section")
req1 = nrql.query("SELECT average(totalTime) from Transaction where appName = 'LB-SPT-BPP-DUBLIN-MBFE-PRD0' and `request.uri` = '/Proxy/auth/user' AND request.method = 'POST'")
for a in req1['results']:
    r1 = round(a['average'], 3)
req2 = nrql.query("SELECT average(totalTime) from Transaction where appName = 'LB-SPT-BPP-DUBLIN-MBFE-PRD0' AND request.method = 'POST' AND request.uri = '/Proxy/v1/placeBet'")
for a in req2['results']:
    r2= round(a['average'], 3)
req3 = nrql.query("SELECT average(totalTime) from Transaction where appName = 'LB-SPT-BPP-DUBLIN-MBFE-PRD0' AND request.uri ='/Proxy/accountHistory' AND request.method = 'GET'")
for a in req3['results']:
    r3 = round(a['average'], 3)
req4 = nrql.query("SELECT percentile(time/1000,96 ) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE 'https://ss-aka-ori%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'LB-SPT-OXYGEN-MBFE-PRD0' AND time<60000")
for a in req4['results']:
    r4= a['percentiles']['96']
req5 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 212371273")
for a in req5['results']:
    r5 = round(a['average'], 3)
req6 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 215068901")
for a in req6['results']:
    r6= round(a['average'], 3)
req7 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 213918623")
for a in req7['results']:
    r7= round(a['average'], 3)
req8 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 213933037")
for a in req8['results']:
    r8 = round(a['average'], 3)
req9 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 239475855")
for a in req9['results']:
    r9 = round(a['average'], 3)
req10 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 239451873")
for a in req10['results']:
    r10 = round(a['average'], 3)
req11 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 211175693")
for a in req11['results']:
    r11 = round(a['average'], 3)
req34 = nrql.query("SELECT average(responseTime) as `Average response time` FROM MobileRequest WHERE (appId = 59921455 OR appVersionId = 59921455)")
for a in req34['results']:
    r12 = round(a['average'], 3)
req35 = nrql.query("SELECT average(responseTime) as `Average response time` FROM MobileRequest WHERE (appId = 66839268 OR appVersionId = 66839268)")
for a in req35['results']:
    r13 = round(a['average'], 3)
r14 = ' '

print ('====================================')
print ("Request Count section")
req12 = nrql.query("SELECT count(*) from Transaction where appName = 'LB-SPT-BPP-DUBLIN-MBFE-PRD0' and `request.uri` = '/Proxy/auth/user' AND request.method = 'POST' ")
for a in req12['results']:
    s1 = a['count']
req13 = nrql.query("SELECT count(*) from Transaction where appName = 'LB-SPT-BPP-DUBLIN-MBFE-PRD0' AND request.method = 'POST' AND request.uri = '/Proxy/v1/placeBet'")
for a in req13['results']:
    s2 = a['count']
req14 = nrql.query("SELECT count(*) from Transaction where appName = 'LB-SPT-BPP-DUBLIN-MBFE-PRD0' AND request.uri ='/Proxy/accountHistory' AND request.method = 'GET'")
for a in req14['results']:
    s3 = a['count']
req15 = nrql.query("SELECT count(*) FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE 'https://ss-aka-ori%' and appName = 'LB-SPT-OXYGEN-MBFE-PRD0'")
for a in req15['results']:
    s4 = a['count']
req16 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'inplay-publisher-prd0'")
for a in req16['results']:
    s5 = round(a['result'])
req17 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'inplay-consumer-prd0'")
for a in req17['results']:
    s6 = round(a['result'])
req18 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'featured-sports-prd0'")
for a in req18['results']:
    s7 = round(a['result'])
req19 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'featured-consumer-prd0'")
for a in req19['results']:
    s8 = round(a['result'])
req20 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'liveserve-publisher-prd0'")
for a in req20['results']:
    s9 = round(a['result'])
req21 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'liveserve-consumer-prd0'")
for a in req21['results']:
    s10 = round(a['result'])
req22 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'lcg-ladbrokesoxygen-prod' and provider  = 'Alb' and displayName = 'cashout-prd0'")
for a in req22['results']:
    s11 = round(a['result'])
req36 = nrql.query("SELECT uniqueCount(sessionId) FROM MobileSession WHERE appVersion ='6.3.0' OR appVersion ='6.0.0'")
for a in req36['results']:
    s12 = a['uniqueCount']
req37 = nrql.query("SELECT uniqueCount(sessionId) FROM MobileSession WHERE appVersion ='7.2 PROD'")
for a in req37['results']:
    s13 = a['uniqueCount']
req23 = nrql.query("SELECT count(*) FROM MobileCrash,MobileHandledException,MobileRequestError where exceptionMessage = 'A JavaScript exception occurred' AND appName = 'LB-SPT-iOS-MBFE-PRD0' AND appVersion = '7.2 PROD'")
for a in req23['results']:
    s14 = a['count']

print ('====================================')
print ("Error Rate section")
t1 = ' '
t2 = ' '
t3 = ' '
req24 = nrql.query("SELECT (percentage(count(*), WHERE status !=200) - percentage(count(*), WHERE status = 404 AND url LIKE '%prd1.api.datafabric.prod.aws%') - percentage(count(*), WHERE status ='success')) as 'error rate'  from PageAction WHERE url  LIKE 'https://ss-aka-ori%' AND actionName = 'Ajax Call' AND  appName ='LB-SPT-OXYGEN-MBFE-PRD0'")
for a in req24['results']:
    t4 = round(a['result'], 3)
req25 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '212371273'")
for a in req25['results']:
    t5 = round(a['result'], 3)
req26 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '215068901'")
for a in req26['results']:
    t6 = round(a['result'], 3)
req27 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '213918623'")
for a in req27['results']:
    t7 = round(a['result'], 3)
req28 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '213933037'")
for a in req28['results']:
    t8 = round(a['result'], 3)
req29 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '239475855'")
for a in req29['results']:
    t9 = round(a['result'], 3)
req30 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '239451873'")
for a in req30['results']:
    t10 = round(a['result'], 3)
req31 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = '211175693'")
for a in req31['results']:
    t11 = round(a['result'], 3)
req32 = nrql.query("SELECT percentage(uniqueCount(sessionId), WHERE category = 'Crash') as `Crash rate` FROM MobileSession, MobileCrash WHERE appName =' LB-SPT-ANDROID-MBFE-PRD0'")
for a in req32['results']:
    t12 = round(a['result'], 3)
req33 = nrql.query("SELECT percentage(uniqueCount(sessionId), WHERE category = 'Crash') as `Crash rate` FROM MobileSession, MobileCrash WHERE appName ='LB-SPT-iOS-MBFE-PRD0'")
for a in req33['results']:
    t13 = round(a['result'], 3)
t14 = ' '

l1 = ['Oxygen Login', 'Oxygen Betplacement', 'Oxygen Bethistory', 'Oxygen SS Averages', 'Oxygen Inplay Publisher MS', 'Oxygen Inplay Consumer MS', 'Oxygen Featured Publisher MS', 'Oxygen Featured Consumer MS', 'Oxygen Liveserv Publisher MS', 'Oxygen Liveserv Consumer MS', 'Oxygen Cashout MS', 'Oxygen Android App Crashes', 'Oxygen iOS App Crashes', 'JavaScript exception occurred']
l2 = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14]
l3 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]
l4 = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14]
for n, i in enumerate(l4):
    if i == 0:
        l4[n] = '< 0,001'

df = DataFrame({'The name of the needed microservice': l1, 'Response time': l2, 'Request count': l3, 'Error Rate': l4})
df.to_excel('/Users/yhrushchynskyi/Downloads/Excel_reports/%s-report.xls' % datetime.datetime.now(), sheet_name='report', index=False)