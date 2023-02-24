import requests

headers = {
    'Content-Type': 'application/json'
}

task_params = {
    'url': 'https://www.instagram.com/p/ChYHpdAvnob/',
  	'target': 'instagram_post',
  	'locale': 'en-us',
  	'geo': 'United States'
}

username = 'username'
password = 'password'
  
response = requests.post(
    'https://scraper-api.smartproxy.com/v1/task',
    headers = headers,
    json = task_params,
    auth = (username, password)
)
print(response.text)