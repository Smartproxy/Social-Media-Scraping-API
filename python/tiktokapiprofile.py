import requests

headers = {
    'Content-Type': 'application/json'
}

task_params = {
    'url': 'https://www.tiktok.com/@nba',
  	'target': 'tiktok_api_profile',
    'count':'20',
    'timestamp':'1681938000'
  	'locale': 'en-us',
  	'geo': 'United States'
}

username = 'username'
password = 'password'
  
response = requests.post(
    'https://scraper-api.smartproxy.com/v2/scrape',
    headers = headers,
    json = task_params,
    auth = (username, password)
)
print(response.text)
