#!/usr/bin/env python3

import requests
import random
import time
import yaml
import os

__dir__ = os.path.dirname(__file__)
config = yaml.safe_load(open(
    os.path.join(__dir__, '..', 'config.yaml')
))

API_URL = config.get('API_URL')
USERNAME = config.get('USERNAME')
PASSWORD = config.get('PASSWORD')
MENTORS = ["جار الله","محمد أحمد عبد الفتاح","صالح","أحمد ناجي","Dr-Taher","Avicenno","Glory20","فيصل","Nehaoua","بندر","فاطمة الزهراء","Dyolf77","Dr. Mohammed","سيف القوضي"]
REASON = 'مرشدك السابق غير متوفر حاليا. قمنا بتعيين مرشد جديد لك!'
s = requests.Session()

def make_request(payload):
    payload['format'] = 'json'
    return s.post(API_URL, data=payload)

def get_token(type='csrf'):
    r = make_request({
        'action': 'query',
        'meta': 'tokens',
        'type': type
    })
    data = r.json()
    return data.get('query', {}).get('tokens', {}).get('%stoken' % type)

make_request({
	"action": "login",
	"lgname": USERNAME,
	"lgpassword": PASSWORD,
	"lgtoken": get_token('login')
})

mentees = open('mentees.txt').read().split('\n')
mentees.pop()
for mentee in mentees:
    mentor = random.choice(MENTORS)
    print("Setting %s's mentor to %s" % (mentee, mentor))
    print(make_request({
        "action": "growthsetmentor",
        "mentee": mentee,
        "mentor": mentor,
        "reason": REASON,
    }).json())
    time.sleep(1)