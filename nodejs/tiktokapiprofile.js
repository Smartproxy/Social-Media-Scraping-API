const request = require('request');

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';

const options = {
  method: 'POST',
  url: 'https://scraper-api.smartproxy.com/v2/scrape',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + Buffer.from(username + ':' + password).toString('base64')
  },
  body: JSON.stringify({
    url: 'https://www.tiktok.com/@nba',
    target: 'tiktok_api_profile',
    count: '20',
    timestamp:'1681938000',
    locale: 'en-us',
    geo: 'United States'
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
