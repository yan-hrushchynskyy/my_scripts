#---------------------------------------------------------------------------
# Script allows to generate report from filtered OpsGenie alerts and send it 
# to MS Teams
#
# v 1.0
#
# Made by Yan Hrushchynskyi 2020
#---------------------------------------------------------------------------

#!/usr/bin/python

import requests, json, sys, os, time
import datetime as dt
from pytz import timezone
import pymsteams

def convert_my_iso_8601(iso_8601, tz_info):
        assert iso_8601[-1] == 'Z'
        iso_8601 = iso_8601[:-1]
        iso_8601_dt = dt.datetime.strptime(iso_8601, '%Y-%m-%dT%H:%M:%S.%f')
        return iso_8601_dt.replace(tzinfo=timezone('UTC')).astimezone(tz_info)


OpsGenie_headers = {'Authorization': 'GenieKey 03c0841c-xxxxxxxxx'}

ops_url =( 'https://api.opsgenie.com/v2/alerts?query=status%3A%20open%20AND%20tag%3A%20(ovp%20AND%20Critical)&limit=100&sort=createdAt&order=desc')

r = requests.get(ops_url, headers=OpsGenie_headers).text
data = json.loads(r)['data']
try:
        for count, alert in enumerate(data, 1):
                alert_tinyId=(alert['tinyId'])
                alert_message=(alert['message'])
                alert_createdAt=(alert['createdAt'])
                alert_owner=(alert['owner'])
                my_dt = convert_my_iso_8601(alert_createdAt, timezone('Israel'))
                f  = open('/home/ec2-user/Yan/msteams_report.txt', 'a')
                print('========  Alert number: ' + str(count) + '  ========', file=f )
                print('\n', file=f)
                print(my_dt, file=f)
                print('\n', file=f)
                print(alert_tinyId + alert_message, file=f)
                print('\n', file=f)
                print("owner: " +  alert_owner, file=f)
                print('\n', file=f)
                f.close()
except:
        f  = open('/home/ec2-user/Yan/msteams_report.txt', 'a')
        print("Some error has been occured, so we have no report", file=f)
        f.close()
finally:
        myfile = open('/home/ec2-user/Yan/msteams_report.txt', 'rt')
        contents = myfile.read()
        myfile.close()
        myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/xxxxxxxx") # webhook ID
        myTeamsMessage.title("This is an hourly OVP critical alerts report ")
        myTeamsMessage.text(contents)
        myTeamsMessage.send()
        print('bzzzzzzzzz for 1 min')
        time.sleep(60)
        myfile = open('/home/ec2-user/Yan/msteams_report.txt', 'r+')
        myfile.truncate(0)
        myfile.close()
sys.exit(0)