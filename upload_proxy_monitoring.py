#---------------------------------------------------------------------------
# Script allows to monitor web upload proxies (modify hosts file, upload  
# sample via selenium, delete sample via API, send alerts to OpsGenie)
#
# v 2.3
#
# Made by Yan Hrushchynskyi 2019
#---------------------------------------------------------------------------

#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time
import logging
import os
import sys
import socket
from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.models import *
from opsgenie.swagger_client.rest import ApiException
from KalturaClient import *
from KalturaClient.Plugins.Core import *
import requests

start_time=time.time()
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename=r'/home/ec2-user/Yan/web_upload_logs.log', level=logging.INFO,format=FORMAT, filemode = 'a')
log = logging.getLogger()
headers = {'Authorization': 'GenieKey 03c0841c-xxxxxxxxxxx'}
configuration.api_key['Authorization'] = '03c0841c-xxxxxxxxxxx'
configuration.api_key_prefix['Authorization'] = 'GenieKey'
client = AlertApi()

partnerId = 111111
config = KalturaConfiguration(partnerId)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
userId = None
ktype = KalturaSessionType.ADMIN
expiry = 432000 # = 5 days
privileges = "disableentitlement"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
wait = WebDriverWait(driver, 20)

def alerttoopsgenie():
        body1 = CreateAlertRequest(
                message='[Web Upload] Problem with uploading on ' + '%s' % i,
                description='Web upload is not working properly on KMS. Please, try to do that manually.\n' \
                'In case real issue contact ProdIT. P.S. This alert will not close automatically\n' \
                'Failed upload proxy: ' + '%s' % i,
                teams=[TeamRecipient(name='Team_Name')],
                visible_to=[TeamRecipient(name='Team_Name', type='team')],
                tags=['NOC', 'Critical'],
                entity='web upload monitoring',
                priority='P1',
                user='my@email.com',
                note='Alert created')

        try:
                response = AlertApi().create_alert(body=body1)
                print('request id: {}'.format(response.request_id))
                print('took: {}'.format(response.took))
                print('result: {}'.format(response.result))
        except ApiException as err:
                print("Exception when calling AlertApi->create_alert: %s\n" % err)

def Selenium():
        try:
                driver.get("https://xxxxxx.mediaspace.kaltura.com/user/login") # account id
                print('Headless Firefox Initialized')
                username = wait.until(ec.presence_of_element_located((By.ID,"Login-username")))
                password = wait.until(ec.presence_of_element_located((By.ID, "Login-password")))
                username.send_keys("user")
                password.send_keys("password")
                btn = wait.until(ec.element_to_be_clickable((By.ID, "Login-login")))
                btn.click()

                driver.get("https://xxxxxx.mediaspace.kaltura.com/upload/media") # account id
                file_input = wait.until(ec.presence_of_element_located((By.ID,"fileinput1")))
                file_input.send_keys("/home/ec2-user/scripts/sample.mp4")
                log.info("File is uploading, waiting for 240 sec")
                time.sleep(240)
                if driver.find_elements_by_xpath("//*[contains(text(), 'Upload Completed')]"):
                        log.info('Everything is OK with ' + '%s' % i)
                        ks = client.session.start(secret, userId, ktype, partnerId, expiry, privileges)
                        client.setKs(ks)
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
                                        log.info(result)
                                        try:
                                                client.media.delete(entry.id)
                                                log.info("Entry was deleted successfully")
                                        except:
                                                result = '0'
                                                log.info('Entry ' + entry.id + ' was not found')
                        if result == '0':
                                log.info("Entry was not found in KMC")
                else:
                        log.info('Upload failed, element was not found')
                        alerttoopsgenie()
                driver.get("https://xxxxxx.mediaspace.kaltura.com/user/logout")
        except:
                print('Login, Upload or Logout failed')
                log.info('Login, Upload or Logout failed')
                alerttoopsgenie()


        finally:
                log.info("Iteration complited")


hosts = ['host1', 'host2', 'host3', 'host4', 'host5'] # our proxy servers
for i in hosts:
        try:
                print(i)
                result1 = (socket.gethostbyname(i))
                result2 = "%s " % result1 + "my.upload.url" # paste your upload URL
                print(result2)
                with open ('/etc/hosts', 'r+') as f:
                        lines = f.read().splitlines()
                        lines[-1] = result2
                        open('/etc/hosts', 'w').write('\n'.join(lines))
                        print("Sleeping for 5 sec")
                        time.sleep(5)
                Selenium()
        except:
                log.info('Web upload script failed')
                alerttoopsgenie()
driver.quit()
response = requests.get('https://api.opsgenie.com/v2/heartbeats/web_upload_mon.py/ping', headers=headers) # OpsGenie Heartbeat
sys.exit(0)
