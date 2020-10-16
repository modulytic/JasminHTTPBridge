# bridge.py
# Noah Sandman <noah@modulytic.com>
# Created 10 October 2020

import os
import json

import urllib
import urllib2

import logging

# MODIFY PREFIX HERE
BRIDGE_PATH = "/root/JasminHTTPBridge"
# DO NOT MODIFY BELOW UNLESS INTENTIONAL

def get_prefix_file(name, mode="r+"):
    global os           # for whatever reason, this script doesn't work without this
    global BRIDGE_PATH
    file_path = os.path.join(BRIDGE_PATH, name)
    return open(file_path, mode)

# enable logging for debugging
logger = logging.getLogger("JasminHTTPBridge")
if len(logger.handlers) != 1:
    hdlr = logging.FileHandler("/var/log/jasmin/http-bridge.log")
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

#logger.info("Got routable: %s" % dir(routable))
#logger.info("Got PDU: %s" % routable.pdu)
#logger.info("Routable ID? %s" % routable.__hash__)

# load config file
conf_opts = {}
conf = get_prefix_file("conf.json")
conf_opts = json.load(conf)
conf.close()

# Round robin load balancer on which endpoint to send it to
endpoint = get_prefix_file("curr_endpoint")
curr_endpoint = int(endpoint.read())
endpoint.seek(0)
endpoint.write(str((curr_endpoint + 1) % len(conf_opts)))
endpoint.truncate()
endpoint.close()

# TODO: Add all supported params here: http://docs.jasminsms.com/en/latest/apis/ja-http/index.html#http-request-parameters
#  SMPP equivalents here: https://www.kannel.org/pipermail/users/2016-April/022812.html
values = {
    "to": routable.pdu.params["destination_addr"],
    "from": routable.pdu.params["source_addr"],
    "content": routable.pdu.params["short_message"],
    "priority": routable.pdu.params["priority_flag"],
    "validity-period": routable.pdu.params["validity_period"]
}
http_data = urllib.urlencode(values)

req = object()
if conf_opts[curr_endpoint]["method"] == "POST":
    req = urllib2.Request(conf_opts[curr_endpoint]["url"], http_data)
elif conf_opts[curr_endpoint]["method"] == "GET":
    req = urllib2.Request(conf_opts[curr_endpoint]["url"] + "?" + http_data)

if req != None:
    urllib2.urlopen(req)
else:
    raise RuntimeError("Invalid HTTP method chosen. Only GET and POST are supported")
