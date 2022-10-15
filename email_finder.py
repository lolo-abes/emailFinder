# Google Cloud API KEY : AIzaSyC1fVY-mUK8hM4mn-vgb8ZkUhWjmULbfrM
# CSE ID : 65672d610066e4c8f
# CENSYS
# API key : 5669609e-8c8e-4a5e-a75a-5c7ba697169a
# Secret : 3IdKh4MGJ4EQ93kzIrqYzr2nuyP53hvW
from modules import (get_company_detail)
from xml import dom
from googleapiclient.discovery import build
import pprint
import json

my_api_key = "AIzaSyC1fVY-mUK8hM4mn-vgb8ZkUhWjmULbfrM"
my_cse_id = "65672d610066e4c8f"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'site:*.fr', my_api_key, my_cse_id, num=10)

for completedomain in results:
    domain=list(completedomain['displayLink'].split('.'))
    domain='.'.join(domain[-2:])
    pprint.pprint("Website Domain : " + completedomain['displayLink'])
    pprint.pprint("Domain : " + domain)
    get_company_detail(domain, True)
    print('\n')
