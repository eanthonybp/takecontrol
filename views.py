from flask import Flask, render_template, redirect, url_for, session, request
from forms import TakeControlForm
import os
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Take Control"


@app.route('/takecontrol',methods=('GET','POST'))
def takecontrol():
    form = TakeControlForm()
    if request.method=='GET':
        return render_template("takecontrol.html", form=form)
        
    if request.method=='POST':
        apicall = "https://www.systemmonitor.us/api/?apikey=%s&service=get_take_control_connection_url&deviceid=%s" % (form.apikey.data,form.deviceid.data)
        xmlresponse = requests.get(apicall)
        root = ET.fromstring(xmlresponse.content)
        connecturl = root[0].text
        
        return redirect(connecturl)
        
@app.route('/tc/<apikey>/<deviceid>/')
def tc(apikey,deviceid):
    apicall = "https://www.systemmonitor.us/api/?apikey=%s&service=get_take_control_connection_url&deviceid=%s" % (str(apikey),str(deviceid))
    xmlresponse = requests.get(apicall)
    root = ET.fromstring(xmlresponse.content)
    connecturl = root[0].text
    return redirect(connecturl)
    
if __name__ == "__main__":
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.debug = True
    app.secret_key = 'SuperSecretKey'
    app.run(host=host,port=port)