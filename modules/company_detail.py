from .config import *
from .utils import format_dict
import requests

# Extracting emails
def get_company_detail(domain, json_output=False):
    url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={email_hunter_api_key}'
    response = requests.get(url)
    json_response = response.json()
    if json_output:
        if response.ok:
            emails_list = json_response['data']['emails']
            if emails_list:
                print("\nExtracted Emails:: ")
                for email in emails_list:
                    print(email['value'])
        else:
            print("\nError while extracting emails using email_hunter_api_key::")
            print(f"Error Description:: {json_response['errors'][0]['details']}.")
