import requests, json
proxy = {
  "http": "http://cis-americas-pitc-alphaz.proxy.corporate.ge.com:80",
  "https" : "http://cis-americas-pitc-alphaz.proxy.corporate.ge.com:80"
}
api_key = 'f09b074388243689d3c090ca064fb0b3'
company = 'synack'
r=requests.get('https://api.crunchbase.com/v/3/organizations?name='+company+'&&&&user_key='+api_key)
output = json.loads(r.content)
print output['data']['items'][0]['properties']['short_description']