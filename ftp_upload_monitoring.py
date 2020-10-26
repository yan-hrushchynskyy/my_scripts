#---------------------------------------------------------------------------
# Script allows to monitor Kaltura FTP (upload sample via FTP, verify if it 
# exists, delete sample via API, send alerts to OpsGenie)
#
# v 3.0
#
# Made by Yan Hrushchynskyi 2019
#---------------------------------------------------------------------------

#!/usr/bin/env python
import ftplib
import sys
import time
import logging
from KalturaClient import *
from KalturaClient.Plugins.Core import *
from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.models import *
from opsgenie.swagger_client.rest import ApiException
import requests
import socket
headers = {'Authorization': 'GenieKey xxxxxxxxx'}
configuration.api_key['Authorization'] = 'xxxxxxx'
configuration.api_key_prefix['Authorization'] = 'GenieKey'
client = AlertApi()
server="FTP server"
user="user"
password="password"
start_time=time.time()
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename=r'/home/ec2-user/Yan/drop_folders_monitoring_script_logs.log', level=logging.INFO,format=FORMAT, filemode = 'a')
log = logging.getLogger()
partnerId = 111111
config = KalturaConfiguration(partnerId)
config.serviceUrl = "https://admin.kaltura.com/"
client = KalturaClient(config)
secret = "xxxxxxxxx"
userId = None
ktype = KalturaSessionType.ADMIN
expiry = 432000 # 432000 = 5 days
privileges = "disableentitlement"

res = (socket.gethostbyname(server))
if res == '1.1.1.1': # paste the relevant IP
        site = 'UA'
elif res == '8.8.8.8':
        site = 'UK'
else:
        site = 'Unknown'

def alerttoopsgenie(body):
        try:
                response = AlertApi().create_alert(body)
                print('request id: {}'.format(response.request_id))
                print('took: {}'.format(response.took))
                print('result: {}'.format(response.result))
        except ApiException as err:
                print("Exception when calling AlertApi->create_alert: %s\n" % err)

body1 = CreateAlertRequest(
        message='[Drop folder] Problem with uploading file to FTP has occurred ' + '%s' % site,
        description='Problem with uploading the file to FTP.\n' \
                                'In case real issue contact ProdIT. P.S. This alert will not close automatically\n' \
                                'FTP site: ' + '%s' % res + ' ' + '%s' % site,
        teams=[TeamRecipient(name='Team_Name')],
        visible_to=[TeamRecipient(name='Team_Name', type='team')],
        tags=['NOC', 'Critical'],
        entity='FTP monitoring',
        priority='P1',
        user='user email',
        note='Alert created')

body3 = CreateAlertRequest(
        message='[Drop folder] Problem with connecting to the FTP server has occurred ' + '%s' % site,
        description='Can not establish the connection with the FTP server or file for upload does not exist. Please, try to do that manually.\n' \
                                'In case real issue contact ProdIT. P.S. This alert will not close automatically\n' \
                                'FTP site: ' + '%s' % res + ' ' + '%s' % site,
        teams=[TeamRecipient(name='Team_Name')],
        visible_to=[TeamRecipient(name='Team_Name', type='team')],
        tags=['NOC', 'Critical'],
        entity='drop folders monitoring',
        priority='P1',
        user='user email',
        note='Alert created')

try:
        session = ftplib.FTP('ftp.kaltura.com','user','password')
        file = open(r'/home/ec2-user/scripts/sample.png', 'rb')
        session.storbinary('STOR sample.png', file)
        log.info('The file was uploaded successfully for %s seconds' % (time.time() - start_time))
        if (time.time() - start_time) > 100:
                log.info('File is uploading too slow, more than 100 sec, alert was created')
                alerttoopsgenie(body1)
except (IOError, KeyboardInterrupt, EOFError, ValueError):
        log.info('File was not uploaded successfully. Error occurred, alert was created')
        alerttoopsgenie(body3)

time.sleep(180)

body2 = CreateAlertRequest(
        message='[Drop folder] Entry in KMC was not found ' + '%s' % site,
        description='Problem with entry in KMC. After uploading file entry was not created. Please,check our KMC account.\n' \
                                'In case real issue contact ProdIT. P.S. This alert will not close automatically.\n' \
                                'FTP site: ' + '%s' % res + ' ' + '%s' % site,
        teams=[TeamRecipient(name='Team_Name')],
        visible_to=[TeamRecipient(name='Team_Name', type='team')],
        tags=['NOC', 'Critical'],
        entity='drop folders monitoring',
        priority='P1',
        user='user email',
        note='Alert created')

def startsession():
        ks = client.session.start(secret, userId, ktype, partnerId, expiry, privileges)
        client.setKs(ks)

def getentries():
        startsession()

        filter = KalturaBaseEntryFilter()
        filter.orderBy = "+createdAt"
        pager = KalturaFilterPager()
        pager.pageSize = 500
        pager.pageIndex = 1

        entrylist = client.media.list(filter, pager)
        result = '0'

        for entry in entrylist.objects:
                if "sample" in entry.name:
                        result = "%i; '%s'; '%s';" % (entry.createdAt, entry.id, entry.name)
                        print (result)
                        try:
                            client.media.delete(entry.id)
                            log.info('Entry was found and deleted successfully')
                        except:
                            result = '0'
                            log.info('Entry ' + entry.id + ' was not found')
        if result == '0':
                alerttoopsgenie(body2)
                log.info('Entry ' + entry.id + ' was not found in KMC, alert was created')

getentries()
response = requests.get('https://api.opsgenie.com/v2/heartbeats/drop_folders_monitoring.py/ping', headers=headers) # OpsGenie Heartbeat
sys.exit(0)
