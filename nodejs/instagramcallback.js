const request = require('request');

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';

const options = {
  method: 'POST',
  url: 'https://scraper-api.smartproxy.com/v2/task',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + Buffer.from(username + ':' + password).toString('base64')
  },
  body: JSON.stringify({
    url: 'https://www.instagram.com/p/ChYHpdAvnob/',
    target: 'instagram_post',
    locale: 'en-us',
    geo: 'United States'
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
