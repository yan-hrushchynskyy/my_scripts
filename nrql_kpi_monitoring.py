#!/usr/local/bin/python3

from nrql.api import NRQL
from pandas import DataFrame
import datetime
import getpass

username = getpass.getuser()
nrql = NRQL()
nrql.api_key = 'xA*********************'
nrql.account_id = '1***66'
since = ' SINCE 1 hours ago'

print('Coral Tech KPI checking. This process will take up to 1 minute')
print ('====================================')
print ("Response time section")
req1 = nrql.query("SELECT average(totalTime) from Transaction where appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' and `request.uri` = '/Proxy/auth/user' AND request.method = 'POST'" + since)
for a in req1['results']:
    r1 = round(a['average'], 3)
req2 = nrql.query("SELECT average(totalTime) from Transaction where appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' AND request.method = 'POST' AND request.uri = '/Proxy/v1/placeBet'" + since)
for a in req2['results']:
    r2= round(a['average'], 3)
req3 = nrql.query("SELECT average(totalTime) from Transaction where appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' AND request.uri ='/Proxy/accountHistory' AND request.method = 'GET'" + since)
for a in req3['results']:
    r3 = round(a['average'], 3)
req4 = nrql.query("SELECT average(time/1000) as 'response time' FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE 'https://ss-aka-ori%' AND payloadSize !=0 and time IS NOT NULL AND appName = 'CR-SPT-OXYGEN-VNL-PRD0' AND time<60000" + since)
for a in req4['results']:
    r4= round(a['average'], 3)
req5 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appName = 'CR-SPT-INPLAYPJFRAM-MBFE-PRD0'" + since)
for a in req5['results']:
    r5 = round(a['average'], 3)
req6 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appName = 'CR-SPT-INPLAYJFRAM-MBFE-PRD0'" + since)
for a in req6['results']:
    r6= round(a['average'], 3)
req7 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 549666821" + since)
for a in req7['results']:
    r7= round(a['average'], 3)
req8 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 99336432" + since)
for a in req8['results']:
    r8 = round(a['average'], 3)
req9 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 216304002" + since)
for a in req9['results']:
    r9 = round(a['average'], 3)
req10 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 96697929" + since)
for a in req10['results']:
    r10 = round(a['average'], 3)
req11 = nrql.query("SELECT average(totalTime) FROM Transaction WHERE appId = 204548170" + since)
for a in req11['results']:
    r11 = round(a['average'], 3)
req34 = nrql.query("SELECT average(responseTime) FROM MobileRequest WHERE appVersionId IN (405683171,414309304)" + since)
for a in req34['results']:
    r12 = round(a['average'], 3)
req35 = nrql.query("SELECT average(responseTime) FROM MobileRequest WHERE appVersionId IN (409932513,425373999,459552512)" + since)
for a in req35['results']:
    r13 = round(a['average'], 3)
req75 = nrql.query("SELECT average(time) from PageAction where appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%performgroup%'" + since)
for a in req75['results']:
    try:
        r14 = round(a['average'], 3)
    except:
        r14 = a['average']
req76 = nrql.query("SELECT average(time) from PageAction where appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%attheraces%'" + since)
for a in req76['results']:
    try:
        r15 = round(a['average'], 3)
    except:
        r15 = a['average']
req77 = nrql.query("SELECT average(`time`) from PageAction where appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%imggaming%'" + since)
for a in req77['results']:
    try:
        r16 = round(a['average'], 3)
    except:
        r16 = a['average']

print ('====================================')
print ("Request Count section")
req12 = nrql.query("SELECT count(*) from Transaction where appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' and `request.uri` = '/Proxy/auth/user' AND request.method = 'POST' " + since)
for a in req12['results']:
    s1 = a['count']
req13 = nrql.query("SELECT count(*) from Transaction where appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' AND request.method = 'POST' AND request.uri = '/Proxy/v1/placeBet'" + since)
for a in req13['results']:
    s2 = a['count']
req14 = nrql.query("SELECT count(*) from Transaction where appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' AND request.uri ='/Proxy/accountHistory' AND request.method = 'GET'" + since)
for a in req14['results']:
    s3 = a['count']
req15 = nrql.query("SELECT count(*) FROM PageAction WHERE actionName = 'Ajax Call' AND url LIKE 'https://ss-aka-ori%' and appName = 'CR-SPT-OXYGEN-VNL-PRD0'" + since)
for a in req15['results']:
    s4 = a['count']
req16 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'inplay-publisher-prd0'" + since)
for a in req16['results']:
    s5 = round(a['result'])
req17 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'inplay-consumer-prd0'" + since)
for a in req17['results']:
    s6 = round(a['result'])
req18 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'featured-sports-prd0'" + since)
for a in req18['results']:
    s7 = round(a['result'])
req19 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'featured-consumer-prd0'" + since)
for a in req19['results']:
    s8 = round(a['result'])
req20 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'liveserve-publisher-prd0'" + since)
for a in req20['results']:
    s9 = round(a['result'])
req21 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'liveserve-consumer-prd0'" + since)
for a in req21['results']:
    s10 = round(a['result'])
req22 = nrql.query("SELECT  sum(`provider.activeConnectionCount.Sum`) / 2 as 'active' FROM LoadBalancerSample WHERE providerAccountName = 'LCG-AWS' and provider  = 'Alb' and displayName = 'cashout-prd0'" + since)
for a in req22['results']:
    s11 = round(a['result'])
req36 = nrql.query("SELECT uniqueCount(sessionId) FROM MobileSession WHERE appVersionId IN (405683171,414309304)" + since)
for a in req36['results']:
    s12 = a['uniqueCount']
req37 = nrql.query("SELECT uniqueCount(sessionId) FROM MobileSession WHERE appVersionId IN (409932513,425373999,459552512)" + since)
for a in req37['results']:
    s13 = a['uniqueCount']
req78 = nrql.query("SELECT count(*) from PageAction where appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%performgroup%'" + since)
for a in req78['results']:
    s14 = a['count']
req79 = nrql.query("SELECT count(*) from PageAction where appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%attheraces%'" + since)
for a in req79['results']:
    s15 = a['count']
req80 = nrql.query("SELECT count(`time`) from PageAction where appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%imggaming%'" + since)
for a in req80['results']:
    s16 = a['count']

print ('====================================')
print ("Error Rate section")
req94 = nrql.query("SELECT filter(count(*), WHERE httpResponseCode NOT IN (200,401) AND error.message is NOT NULL) * 100 / filter(count(*), WHERE duration IS NOT NULL) as 'BPP login error rate' FROM Transaction,TransactionError WHERE request.uri = '/Proxy/auth/user' AND appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0'" + since)
for a in req94['results']:
    t1 = round(a['result'], 3)
req105 = nrql.query("SELECT filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and bet NOT LIKE '%isConfirmed%:Y%' and bet NOT LIKE '%OpenBetBir%' and serviceName = 'placeBet' and betError  NOT LIKE '%PRICE_CHANGED%' AND betError NOT LIKE '%OUTCOME_SUSPENDED%' AND betError NOT LIKE '%STAKE_TOO_HIGH%' and betError NOT LIKE '%LIVE_PRICE_UNAVAILABLE%' AND betError NOT LIKE '%PT_ERR_RG_SESSION_TIMER%' AND betError NOT LIKE '%EXTERNAL_FUNDS_UNAVAILABLE%' and error NOT LIKE '%EXTERNAL_FUNDS_UNAVAILABLE%' AND betError NOT LIKE '%INSUFFICIENT_FUNDS%' and actionName NOT LIKE '%retryTrigger%' and error IS NOT NULL and error  LIKE '%isTrusted%:true%' and error NOT LIKE '%UNAUTHORIZED_ACCESS%')*100/(filter(count(*),  WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and bet NOT LIKE '%isConfirmed%:Y%' and serviceName = 'placeBet' and betError LIKE '%PRICE_CHANGED%' or bet LIKE '%OpenBetBir%' or betError LIKE '%OUTCOME_SUSPENDED%' OR  betError LIKE '%STAKE_TOO_HIGH%' or betError LIKE '%LIVE_PRICE_UNAVAILABLE%' or betError LIKE '%PT_ERR_RG_SESSION_TIMER%' or betError LIKE '%EXTERNAL_FUNDS_UNAVAILABLE%' or error LIKE '%EXTERNAL_FUNDS_UNAVAILABLE%' or betError LIKE '%INSUFFICIENT_FUNDS%' or actionName LIKE '%retryTrigger%' or (error IS NOT NULL and error  LIKE '%isTrusted%:true%') or error  LIKE '%isTrusted%:true%' or error LIKE '%UNAUTHORIZED_ACCESS%' AND  status !=500) + filter(count(*),  WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and bet NOT LIKE '%isConfirmed%:Y%' and bet NOT LIKE '%OpenBetBir%' and serviceName = 'placeBet' and betError  NOT LIKE '%PRICE_CHANGED%' AND betError NOT LIKE '%OUTCOME_SUSPENDED%' AND betError NOT LIKE '%STAKE_TOO_HIGH%' and betError NOT LIKE '%LIVE_PRICE_UNAVAILABLE%' AND betError NOT LIKE '%PT_ERR_RG_SESSION_TIMER%' AND betError NOT LIKE '%EXTERNAL_FUNDS_UNAVAILABLE%' and error NOT LIKE '%EXTERNAL_FUNDS_UNAVAILABLE%' AND betError NOT LIKE '%INSUFFICIENT_FUNDS%' and actionName NOT LIKE '%retryTrigger%' and error IS NOT NULL and error  LIKE '%isTrusted%:true%' and error NOT LIKE '%UNAUTHORIZED_ACCESS%') + filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' AND (actionName = 'PlaceBetSuccess' and bet LIKE '%receipt%') OR  actionName = 'quickBetService=>placeBet=>Success' OR (url LIKE '%v1/placeWinPoolBet%' AND payloadSize > 10) or (actionName = 'yourcallBetslipService=>placeBet=>Success' AND betID IS NOT NULL))) as 'error rate(%)' FROM  PageAction" + since)
for a in req105['results']:
    t2 = round(a['result'], 3)
req95 = nrql.query("SELECT filter(count(*), WHERE request.uri ='/Proxy/accountHistory' AND request.method = 'GET' and httpResponseCode NOT IN (200,401)) * 100 / filter(count(*), WHERE request.uri ='/Proxy/accountHistory' AND request.method = 'GET') as 'acc history error rate' from Transaction WHERE appName = 'CR-SPT-BPP-MBFE-DBLN-PRD0' EXTRAPOLATE" + since)
for a in req95['results']:
    t3 = round(a['result'], 3)
req24 = nrql.query("SELECT (percentage(count(*), WHERE status !=200) - percentage(count(*), WHERE status = 404 AND url LIKE '%prd1.api.datafabric.prod.aws%') - percentage(count(*), WHERE status ='success')) as 'error rate'  from PageAction WHERE url  LIKE 'https://ss-aka-ori%' AND actionName = 'Ajax Call' AND  appName ='CR-SPT-OXYGEN-VNL-PRD0'" + since)
for a in req24['results']:
    t4 = round(a['result'], 3)
req25 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 101590707  EXTRAPOLATE" + since)
for a in req25['results']:
    t5 = round(a['result'], 3)
req26 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 96697357" + since)
for a in req26['results']:
    t6 = round(a['result'], 3)
req27 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 549666821 EXTRAPOLATE" + since)
for a in req27['results']:
    t7 = round(a['result'], 3)
req28 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 99336432 EXTRAPOLATE" + since)
for a in req28['results']:
    t8 = round(a['result'], 3)
req29 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 216304002" + since)
for a in req29['results']:
    t9 = round(a['result'], 3)
req30 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 96697929" + since)
for a in req30['results']:
    t10 = round(a['result'], 3)
req31 = nrql.query("SELECT filter(count(*), WHERE error.message IS NOT NULL)*100 / filter(count(*), WHERE duration IS NOT NULL) as 'ErrorRate' FROM Transaction,TransactionError WHERE appId = 204548170 EXTRAPOLATE" + since)
for a in req31['results']:
    t11 = round(a['result'], 3)
req32 = nrql.query("SELECT percentage(uniqueCount(sessionId), WHERE category = 'Crash') as `Crash rate` FROM MobileSession, MobileCrash WHERE appVersionId IN (405683171,414309304)" + since)
for a in req32['results']:
    t12 = round(a['result'], 3)
req33 = nrql.query("SELECT percentage(uniqueCount(sessionId), WHERE category = 'Crash') as `Crash rate` FROM MobileSession, MobileCrash WHERE appVersionId IN (409932513,425373999,459552512)" + since)
for a in req33['results']:
    t13 = round(a['result'], 3)
req66 = nrql.query("SELECT filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%perform%wab%' AND status NOT IN (200,401)) * 100 / filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%perform%wab%') from PageAction" + since)
for a in req66['results']:
    t14 = a['result']
req67 = nrql.query("SELECT filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%attheraces%' AND status NOT IN (200,401)) * 100 / filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%attheraces%') from PageAction" + since)
for a in req67['results']:
    t15 = a['result']
req68 = nrql.query("SELECT filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%imggaming%' AND status NOT IN (200,401)) * 100 / filter(count(*), WHERE appName = 'CR-SPT-OXYGEN-VNL-PRD0' and url like '%imggaming%') from PageAction" + since)
for a in req68['results']:
    try:
        t16 = round(a['result'], 3)
    except:
        t16 = a['result']


l1 = ['Oxygen Login', 'Oxygen Betplacement', 'Oxygen Bethistory', 'Oxygen SS Averages', 'Oxygen Inplay Publisher MS', 'Oxygen Inplay Consumer MS', 'Oxygen Featured Publisher MS', 'Oxygen Featured Consumer MS', 'Oxygen Liveserv Publisher MS', 'Oxygen Liveserv Consumer MS', 'Oxygen Cashout MS', 'Oxygen Android App Crashes', 'Oxygen iOS App Crashes', 'Streaming - Perform', 'Streaming - ATR', 'Streaming - IMG']
l2 = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16]
l3 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]
l4 = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16]
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
    df.to_excel('/Users/' + username + '/Downloads/Excel_reports/%s-report.xls' % datetime.datetime.now(), sheet_name='report', index=False)
    print('Check your directory. Report should be ready')
except:
    print ('Contact Yan. There is something wrong with reports generating')