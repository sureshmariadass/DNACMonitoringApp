import json
from requests.exceptions import Timeout
from requests.auth import HTTPBasicAuth
import requests

DEF_TIMEOUT = 5
uname="admin"
pword="C1sc0123"
requests.packages.urllib3.disable_warnings()
ip="10.171.92.10"

data=[]

def get_token():
    post_url = "https://"+ip+"/dna/system/api/v1/auth/token"

    headers = {'content-type': 'application/json',}

    try:
        r = requests.post(post_url, auth=HTTPBasicAuth(uname, pword), headers=headers, verify=False, timeout=DEF_TIMEOUT)
    except Timeout as e:
        raise Timeout(e)
    except:
        raise BaseException('Something went wrong while getting access token')
    else:
        response_data = r.json()
        #print(response_data)
        if 'Token' in response_data.keys():
            return response_data['Token']
        elif 'exp' in response_data.keys():
            raise PermissionError(response_data['exp'] + '.')
        elif 'errorCode' in response_data.keys() and response_data['errorCode'] == 'INVALID_CREDENTIALS':
            raise PermissionError(response_data['detail'] + '. ' + response_data['message'])
        #"error": "Authentication has failed. Please provide valid credentials."

def get_device_list(token):
    url="https://"+ip+"/dna/intent/api/v1/network-device"
    header = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=header,verify=False, timeout=DEF_TIMEOUT)
    device_list = resp.json()
    return device_list

def get_device_detail(token,macAd):
    url="https://"+ip+"/dna/intent/api/v1/device-detail/?searchBy="+macAd+"&identifier=macAddress"
    header = {'x-auth-token': token, 'content-type' : 'application/json'}
    resp = requests.get(url, headers=header,verify=False, timeout=DEF_TIMEOUT)
    device_detail = resp.json()
    return device_detail

if __name__ == "__main__":
    token=get_token()
    device_list=get_device_list(token)
    for mac in device_list['response']:
        macAd=mac['macAddress']
        dev_det=get_device_detail(token,macAd)
        data.append(dev_det)
    print(json.dumps(data))
