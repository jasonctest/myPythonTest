#!/bin/sh
'''
with open('data.txt') as f:
     lines = f.readlines()

print(lines,)
'''

'''
lines = [line.strip() for line in open('data.txt')]

print(lines[1:])
'''

'''
import json
weather = urllib2.urlopen('url')
wjson = weather.read()
wjdata = json.loads(wjson)
print wjdata['data']['current_condition'][0]['temp_C']

#wjdata = json.load(urllib2.urlopen('url'))

'''

'''
import requests
import json
from pyjq import *
#myurl='http://api.twitter.com/1/statuses/public_timeline.json'

myurl='http://223.6.252.216/1.0/search?q=%E4%BA%94%E5%AD%90%E6%A3%8B&fix_spelling=1&limit=100&page=0&include_descriptions=0&include_snippets=0&include_screenshots=0&include_platforms=0&include_developers=0&include_editions=1&channel=serp-list&skip=0&platform_ids=[2005]&locale=zh_CN&partner_id=2877241536&partner_secret=w3cqhpsem7tevqfw6ket2r8azug8cwsq&stores=[%22yunos%22]'


wjdata = requests.get(myurl).json()
#jq(".").transform("42") == "42"
#print wjdata['data']['current_condition'][0]['temp_C']

print(json.dumps(wjdata ['results'][0]))

#import subprocess
#proc = subprocess.Popen('jq' + 'wjdata', shell = True, stderr = subprocess.STDOUT,stdout=subprocess.PIPE,stdin = subprocess.PIPE)
#proc_read = proc.stdout.read()
#print(proc)
'''

'''
import json

with open("json_data.json") as f:
	#wjson = f.read()
	jdata = json.load(f)

print(jdata[1])
'''

import urllib2
import json, requests

myurl='http://223.6.252.216/1.0/search?q=%E4%BA%94%E5%AD%90%E6%A3%8B&fix_spelling=1&limit=100&page=0&include_descriptions=0&include_snippets=0&include_screenshots=0&include_platforms=0&include_developers=0&include_editions=1&channel=serp-list&skip=0&platform_ids=[2005]&locale=zh_CN&partner_id=2877241536&partner_secret=w3cqhpsem7tevqfw6ket2r8azug8cwsq&stores=[%22yunos%22]'

#response = urllib2.urlopen(myurl)
response = requests.get(myurl)
#print response.json 
data = response.text
print data["results"][0]

