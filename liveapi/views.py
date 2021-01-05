from django.shortcuts import render

from liveapi.api import api

# Create your views here.
def device_list(request):
    
    token=api.get_token()
    device_list=api.get_device_list(token)

    return render(request,'list_of_device.html',{'device_list':device_list['response']})

def cpu_utilization(request):
	data=[]
	token=api.get_token()
	device_list=api.get_device_list(token)
	for mac in device_list['response']:
		macAd=mac['macAddress']
		dev_det=api.get_device_detail(token,macAd)
		data.append(dev_det)
	return render(request,'cpu_ut.html',{'device_detail':data})

def memory_utilization(request):
	data=[]
	token=api.get_token()
	device_list=api.get_device_list(token)
	for mac in device_list['response']:
		macAd=mac['macAddress']
		dev_det=api.get_device_detail(token,macAd)
		data.append(dev_det)
	return render(request,'memory_ut.html',{'device_detail':data})