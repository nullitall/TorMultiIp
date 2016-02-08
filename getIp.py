import socket
import socks
import json
import urllib2
import sys

ipcheck_url = 'http://checkip.amazonaws.com/'
# Actual IP.
#print(urllib2.urlopen(ipcheck_url).read())

# Tor IP.
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', int(sys.argv[1]))
socket.socket = socks.socksocket
ip  = (urllib2.urlopen(ipcheck_url).read())

url = 'http://freegeoip.net/json/'
country  = json.loads(urllib2.urlopen(url).read())['country_name']
print ip + " ----" + country
