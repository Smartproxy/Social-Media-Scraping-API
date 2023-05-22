import requests

headers = {
    'Content-Type': 'application/json'
}

task_params = {
    'query': 'tasty',
  	'target': 'tiktok_api_hashtag',
    'count': '15',
    'cursor':'10',
  	'locale': 'en-us',
  	'geo': 'United States'
}

username = 'username'
password = 'password'
  
response = requests.post(
    'https://scraper-api.smartproxy.com/v1/scrape',
    headers = headers,
    json = task_params,
    auth = (username, password)
)
print(response.text)