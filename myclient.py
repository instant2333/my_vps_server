import json
import requests
from flask import Flask,request,Response

dict={}
dict["coin_name"]=input()
dict["period"]=input()
dict["size"]=input()
json.dumps(dict)
print(dict)
#url="http://103.114.160.243:4001/static/zecusdt2019-09-08%2018.16.json"
url="http://127.0.0.1:5000/"
r=requests.post(url,dict)
print(r)
