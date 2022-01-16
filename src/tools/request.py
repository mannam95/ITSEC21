#!/usr/bin/python

import sys
import base64
import json
import requests

if ( len(sys.argv) != 3 ):
    print 'Usage: python request.py <fingerprint_image_1> <fingerprint_image_2>'
    sys.exit(0)

img1_base64 = base64.b64encode(open(sys.argv[1], "rb").read())
img2_base64 = base64.b64encode(open(sys.argv[2], "rb").read())	

url = "http://141.44.30.186:5001/api/verifinger"
headers = {'Content-type': 'application/json'}
data = {'im1': img1_base64, 'im2': img2_base64}

r = requests.post(url, data=json.dumps(data), headers=headers)

print r,r.json()
