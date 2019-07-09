import json
from flask import Flask,request,Response
import os,sys,string

basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)

app.run(   
  host='0.0.0.0',
  port= 4000
  )
