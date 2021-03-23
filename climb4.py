import os
import json
import urllib2

'''proc = subprocess.Popen('', stdout=subprocess.PIPE)
output = proc.stdout.read()
print output'''
 
sudoPassword = 'diko'
command = 'tshark -i ens33 -T fields -e ip.addr -e tcp.dstport -e tcp.srcport -e tcp.analysis.ack_rtt -e frame.time_epoch -E aggregator=/s '
p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))


'''data = {
        'username': 'diko',
        'password':'diko'
}

req = urllib2.Request('http://localhost:5555/login')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))'''

