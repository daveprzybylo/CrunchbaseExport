#################
# Crunchbase V3 parser
# Usage: 'python main.py CompanyYouWantInfoOn'
# Created by Dave PryzHELLO and Kyle LePrevost
#################

import requests 
import json
import os
import sys

# Grab proxy settings and the API key from our environment
proxy = os.environ.get('https_proxy')
api_key = os.environ.get('crunchbaseexport')

# The company is set via a command line argument
company = sys.argv[1]

# This function grabs the company 
def get_company_data(api_key, company):
	# Make the API call and load the JSON
	api_call = requests.get('https://api.crunchbase.com/v/3/organizations?name='+company+'&&&&user_key='+api_key)
	raw_json = json.loads(api_call.text)
	# Parsing JSON to return the information we crave
	company_description = raw_json['data']['items'][0]['properties']['short_description']
	company_name = raw_json['data']['items'][0]['properties']['name']
	company_location = raw_json['data']['items'][0]['properties']['city_name']+', '+raw_json['data']['items'][0]['properties']['region_name']+', '+raw_json['data']['items'][0]['properties']['country_code']
	# Printing out results
	print company_name
	print company_description
	print company_location
	
	
get_company_data(api_key, company)