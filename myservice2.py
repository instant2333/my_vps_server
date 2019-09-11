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
    time1=temp+datetime.datetime.now().strftime('%Y-%m-%d %H.%M')
    filepath="static/"+time1+".json"
    with open(filepath,'w+') as file_obj:
      json.dump(api.get_kline(temp,period,size),file_obj)

@app.route('/api/getcoin', methods=['GET','POST'])
def getcoin():
    if request.method == 'POST' and request.is_json:
        coin_name = request.get_json()['coin_name']
        period=request.get_json()['period']
        size=request.get_json()['size']
        result=api.get_kline(coin_name, period, size)
        print(coin_name,period,size)
        print(result)
        return Response(
            result,
            mimetype='application/json',
            headers={
                'Cache-Control': 'no-cache',
                'Access-Control-Allow-Origin': '*'
            }
        )

if __name__ == "__main__":
  app.run(
    host='0.0.0.0',
    port= 4008,
    debug=True
    )
