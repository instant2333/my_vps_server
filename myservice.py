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
  for temp in symbol:
    time1=temp+datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    filepath="static/"+time1+".json"
    with open(filepath,'w+') as file_obj:
      json.dump(api.get_kline(symbol,period,size),file_obj)
      #json.dump({'1':filepath}, file_obj)

scheduler = BackgroundScheduler()
scheduler.add_job(getdata,'interval',seconds=120,args=[["btcusdt","ethusdt","xrpusdt","ltcusdt","bchusdt","eosusdt","etcusdt","adausdt"],"1min",3])
scheduler.start()

if __name__ == "__main__":
  app.run(
    host='0.0.0.0',
    port= 4000,
    debug=True
    )


