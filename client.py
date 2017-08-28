import os 
import socket, struct
import subprocess
import sys
import argparse
import re
import datetime
from datetime import datetime
import time
import json
from bson import json_util
import urllib2
from time import mktime


del sys.argv[0]
sys.argv.insert(0,'python')
sys.argv.insert(1,'climb4.py')
 
#citrix_ip = struct.unpack("!I", socket.inet_aton("ipaddress"))[0]
#shop_ip=struct.unpack("!I", socket.inet_aton("ipaddress"))[0]

proc = subprocess.Popen(sys.argv,stdout=subprocess.PIPE)
for line in iter(proc.stdout.readline,''):
            #print "entered for loop"
            b = line.strip().split()
            if len(b)==6:
	      src_ipaddr=b[0]
	      #s = struct.unpack("!I", socket.inet_aton(src_ipaddr))[0]
	      dst_ipaddr=b[1]
	      #d = struct.unpack("!I", socket.inet_aton(dst_ipaddr))[0]
	      src_port=b[2]
	      dst_port=b[3]
              rtt_value = float(b[4])
	      #rtt_value=float(b[4])
	      print "rtt_value",rtt_value
              #timestamp=b[5].join('')
	      c = int(re.sub("\.", "", b[5]))
              #c= float(b[5])
               
              #samayam = float(b[5])
              #print timestamp
              #samayam = datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
              #samayam = json.dumps(timestamp, default=json_util.default)
              #print "timestamp=",timestamp
	      #samayam = datetime.utcfromtimestamp(timestamp)
              #c = int(mktime(samayam.timetuple()))*1e9
              #e = int(mktime(samayam.timetuple()))
              #$d = 
              #c = int(d)
              data = {
                  'rtt_value': rtt_value,
                  'src_ipaddr':src_ipaddr,
                  'dst_ipaddr':dst_ipaddr,
                  'c':c,
              }

              req = urllib2.Request('http://localhost:portnumber/login')
              req.add_header('Content-Type', 'application/json')
              response = urllib2.urlopen(req, json.dumps(data))

              #response = urllib2.urlopen(req, json.dumps(data, default=json_util.default))
              #try:
               #  response = urllib2.urlopen(req, json.dumps(data))
              #except urllib2.HTTPError:
              #   pass




