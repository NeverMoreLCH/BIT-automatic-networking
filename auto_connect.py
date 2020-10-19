import os
import sys
import requests
import time

username = ''
password = ''
user_ip  = ''
ping_url = 'http://39.98.145.168'
reconnect_time = 90

def isConnected1():
	try:
		html = requests.get("http://www.baidu.com",timeout=2)
	except:
		return False
	return True

def isConnected2():
    try:
        html = requests.get(ping_url,timeout=10)
    except:
        return False
    else:
        if 'Yee' in html.text:
            return True
        return False

def connect_method1():
    os.system('curl --data "action=login&username=' + username + '&password=' + password + '&ac_id=1&user_ip=' + user_ip + '&nas_ip=0.0.0.0&user_mac=00:00:00:00:00:00&save_me=0&ajax=1" http://10.0.0.55:801/include/auth_action.php')

def connect_method2():
    url = "http://10.0.0.55:801/include/auth_action.php"
    data = {"action":"login",
            "username": username,
            "password": password, 
            "ac_id": "1",
            "user_ip": user_ip, 
            "nas_ip": "0.0.0.0",
            "user_mac": "00:00:00:00:00:00",
            "save_me": "1",
            "ajax": 1}
    res = requests.post(url=url,data=data)
    # print(res.text)

flag = 0
while (True):
	if time.time() - flag >= reconnect_time:
		flag = time.time()
		if not isConnected2():
				connect_method2()
		print(flag, isConnected2())
