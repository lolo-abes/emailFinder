# Google Cloud API KEY : AIzaSyC1fVY-mUK8hM4mn-vgb8ZkUhWjmULbfrM
# CSE ID : 65672d610066e4c8f

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
    'mail site:*.fr', my_api_key, my_cse_id, num=10)
# for result in results:
#     pprint.pprint(result)

# returns JSON object as 
# a dictionary
# data = json.load(results)
  
# Iterating through the json
# list
for i in results:
    pprint.pprint(i['displayLink'])
# for i in data['title']:
#     pprint.pprint(result)