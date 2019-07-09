import json
from flask import Flask,request,Response
import os,sys,string
import HuobiServices as api
import apscheduler
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)

def getdata(symbol,period,size=1):
  time1="btc"+datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
  filepath="static/"+time1+".json"
  with open(filepath,'w+') as file_obj:
    json.dump(api.get_kline(symbol,period,size),file_obj)
    #json.dump({'1':filepath}, file_obj)


scheduler = BackgroundScheduler()
scheduler.add_job(getdata,'interval',seconds=3,args=["btcusdt","1min",1])
scheduler.start()
