# bridge.py
# Noah Sandman <noah@modulytic.com>
# Created 10 October 2020

import os
import json

import urllib
import urllib2

# MODIFY PREFIX HERE
BRIDGE_PATH = "/root/JasminHTTPBridge"
# DO NOT MODIFY BELOW UNLESS INTENTIONAL

conf_opts = {}
conf_path = os.path.join(bridge_path, "conf.json")
with open(conf_path) as conf_f:
    conf_opts = json.load(conf_f)

# TODO: Add all supported params here: docs.jasminsms.com/en/latest/apis/ja-http/index.html#http-request-parameters
values = {
    "to": routable.pdu.params['destination_addr'],
    "from": routable.pdu.params['source_addr'],
    "content": routable.pdu.params['short_message']
}
http_data = urllib.urlencode(values)

req = object()
if conf_opts.method == "POST":
    req = urllib2.Request(conf_opts["url"], http_data)
elif conf_opts.method == "GET":
    req = urllib2.Request(conf_opts["url"] + "?" + http_data)

if req != None:
    urllib2.urlopen(req)
else:
    raise RuntimeError("Invalid HTTP method chosen. Only GET and POST are supported")