# encoding = utf-8

import os
import sys
import time
import datetime
import requests
import urllib3
import json

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


# Cisco DNA Center info

username = 'admin'
password = 'C1sc0123'
DNAC_URL = 'https://10.91.91.172'


DNAC_AUTH = HTTPBasicAuth(username, password)


def get_dnac_jwt_token(dnac_auth):
    """
    Create the authorization token required to access DNA C
    Call to Cisco DNA Center - /api/system/v1/auth/login
    :param dnac_auth - Cisco DNA Center Basic Auth string
    :return: Cisco DNA Center JWT token
    """
    url = DNAC_URL + '/dna/system/api/v1/auth/token'
    header = {'content-type': 'application/json'}
    response = requests.post(url, auth=dnac_auth, headers=header, verify=False)
    dnac_jwt_token = response.json()['Token']
    return dnac_jwt_token


def get_all_device_info(dnac_jwt_token):
    
    url = DNAC_URL + '/dna/intent/api/v1/network-device'
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    all_devices_response = requests.get(url, headers=header, verify=False)
    all_devices_json = all_devices_response.json()
    all_devices_info = all_devices_json['response']
    return all_devices_info


def get_overall_network_health(dnac_jwt_token):
    
    epoch_time = get_epoch_current_time()
    url = DNAC_URL + '/dna/intent/api/v1/network-health?timestamp=' + str(epoch_time)
    header = {'content-type': 'application/json', 'x-auth-token': dnac_jwt_token}
    network_health_response = requests.get(url, headers=header, verify=False)
    network_health_json = network_health_response.json()
    network_health = network_health_json['response'][0]['healthScore']
    return network_health


def get_epoch_current_time():
    """
    This function will return the epoch time for the {timestamp}
    :return: epoch time including msec
    """
    epoch = time.time()*1000
    return int(epoch)


def main():
    # get the Cisco DNA Center Auth
    dnac_auth = get_dnac_jwt_token(DNAC_AUTH)

    # get all the devices info
    all_devices_info = get_all_device_info(dnac_auth)
    print("all device info")
    print(json.dumps(all_devices_info))
    print("----------------")
    # get the overall network health
    overall_network_health = get_overall_network_health(dnac_auth)
    print(json.dumps([{'overall_network_health': overall_network_health}]))


if __name__ == '__main__':
    main()


