# Google Cloud API KEY : AIzaSyC1fVY-mUK8hM4mn-vgb8ZkUhWjmULbfrM
# CSE ID : 65672d610066e4c8f
# CENSYS
# API key : 5669609e-8c8e-4a5e-a75a-5c7ba697169a
# Secret : 3IdKh4MGJ4EQ93kzIrqYzr2nuyP53hvW

# Search email adresses through Censys by request : location.province:Occitanie and location.city:Montpellier and services.port:80 or services.port:443

from modules import (get_company_detail)
from xml import dom
from googleapiclient.discovery import build
import pprint
import json
from censys.search import CensysHosts

my_api_key = "AIzaSyC1fVY-mUK8hM4mn-vgb8ZkUhWjmULbfrM"
my_cse_id = "65672d610066e4c8f"

h = CensysHosts()

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
    query = h.search(str(domain) + " and location.province:Occitanie", per_page=1)
    domain_lookup_result = query()
    if domain_lookup_result:
        pprint.pprint("Location Domain : " + domain_lookup_result[0]['location']['city'] + " " + domain_lookup_result[0]['location']['postal_code'] + " " + domain_lookup_result[0]['location']['province'])
        pprint.pprint("Machine founded : " + str(''.join(domain_lookup_result[0]['dns']['reverse_dns']['names'])))
        if domain_lookup_result[0]['location']['province'] == "Occitanie":
            get_company_detail(domain, True)
    print('\n')
