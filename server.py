from flask import Flask, request, render_template, g
import json
import subprocess
import MySQLdb
from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError

app = Flask(__name__)

db = MySQLdb.connect("localhost","user","pwd","dbname" )
cursor = db.cursor()

host='localhost'
port=8086
metric = "rating"
series = []
USER = 'user'
PASSWORD = 'pwd'
DBNAME = 'dbname'

def insert_readings(rtt_value,src_ipaddr,dst_ipaddr,c):
      client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
      #time = datetime.utcfromtimestamp(samayam)
      #mylist = list()
      #mylist.append(username)
      #for i in mylist:
       #   print i
          
      pointValues = {
                    "measurement": metric,
                    "time":c,
                    'fields':  {
                    'rtt_value':rtt_value ,
                    
          
                    
                     },
                     'tags': {
                       'src_ipaddr':src_ipaddr,
                       'dst_ipaddr':dst_ipaddr,
                       
                      },
      }
      series=[pointValues]
      print series
      client.write_points(series)
      result = client.query('select value from rating;')
      print("Result: {0}".format(result))
      return series  

def insert_status(src_ipaddr,dst_ipaddr,status):
    sql = "INSERT INTO info(src_ipaddr,dst_ipaddr,status) VALUES ('%s','%s','%s')" %(src_ipaddr,dst_ipaddr,status)
    cursor.execute(sql)
    db.commit()
    return "done"  
      

@app.route('/login',methods=['POST'])
def login():
     rtt_value = request.json['rtt_value']
     #username = request.json('username', type=int)
     src_ipaddr = request.json['src_ipaddr']
     dst_ipaddr = request.json['dst_ipaddr']
     c = request.json['c']
     
     #time = datetime.utcfromtimestamp(samayam)	
     
     insert_readings(rtt_value,src_ipaddr,dst_ipaddr,c)
     
     if rtt_value < threshold value:
        status = "below threshold"
        #insert_status(status)
     elif rtt_value > threshold value:
        status = "above threshold"
     insert_status(src_ipaddr,dst_ipaddr,status)
        #insert_status(status)
     return "Done"




if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=port number)
