
# Social Media Scraping API

[<img src="https://i.imgur.com/eViepgO.png">](https://dashboard.smartproxy.com/register?page=social-media%2Fpricing&utm_source=socialorganic&utm_medium=social&utm_campaign=github_some_scraper) 

[![](https://dcbadge.vercel.app/api/server/gvJhWJPaB4)](https://discord.gg/sCr34yVDVB)

## List of contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Synchronous (real-time) & asynchronous (callback) requests](#synchronous)
- [Instagram](#instagram)
- [TikTok](#tiktok)
- [Targets](#targets)
- [Parameters](#parameters)
- [Postman Collection](#postman-collection)
- [License](#license)

## Introduction

With our Social Media Scraping API, you can gather most important data from Social Media websites. Currently supporting Instagram and TikTok.

## Authentication

Once you have an active Social Media Scraping API subscription, you can set your password in the dashboard. To do so, select **Social Media** under **Scraping APIs** list. Then, head over to the **Authentication method** tab. Click the pencil icon and enter your password.

## Synchronous (real-time) & asynchronous (callback) requests <a name="synchronous"></a>

With Social Media Scraping API, you can scrape choosing synchronous requests to receive data instantly or asynchronous requests to receive data based on a callback function.

### Synchronous (real-time)

```http
POST
https://scraper-api.smartproxy.com/v2/scrape
```

### Asynchronous (create a callback)

```http
POST
https://scraper-api.smartproxy.com/v2/task
```

### Asynchronous (receive data in raw HTML)

```http
GET
https://scraper-api.smartproxy.com/v2/task/{{task_id}}/results?type=raw
```

### Asynchronous (receive data parsed in JSON)

```http
GET
https://scraper-api.smartproxy.com/v2/task/{{task_id}}/results?type=Parsed
```

## Instagram

Instagram can be targeted using direct URL.

The `instagram_post`, `instagram_profile`, and `instagram_reel` targets allow you to scrape Instagram's HTML and receive data parsed in JSON.

The `instagram_graphql_post`, `instagram_graphql_profile` and `instagram_graphql_hashtag` target allows you to scrape Instagram's GraphQL API endpoint and receive data parsed in JSON.

### Instagram profile

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/nba)
```target``` (in this example, instagram_profile)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram profile URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |


### Response

First 2 top & bottom ads and product listing info
```http
           {
    "data": {
        "content": {
            "account": {
                "username": "nba",
                "verified": true
            },
            "stats": {
                "posts": "56,793",
                "followers": "76.5M",
                "following": "1,108"
            },
            "biography": {
                "name": "NBA",
                "occupation": "Sports league",
                "description": "FRIDAY on ESPN ⤵️\n7:30pm/et: HEAT/BUCKS\n10:00pm/et: THUNDER/SUNS",
                "url": "linkin.bio/nba"
            },
            "posts": [
                {
                    "href": "https://www.instagram.com/p/CpCLWcSMTxa/",
                    "description": "18 teams in action, 9 winners Thursday night!",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332394535_1174583859869004_5699117325227109932_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=T73dZU-MUfoAX9IX02X&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCxqyoh2w8UI6PujgGmyzJ4Kmi5thgX6pCarwcnsn7PkQ&oe=63FCF30F&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCLT9Ps1CP/",
                    "description": "43 for @laurimarkkanen in the OT W!",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332566741_1254687808779337_9193264579495047501_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=T2jea-Ab0O0AX8uQmbV&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfD6iiM7_ss2K1VQ4LHyoX_325WVdvUMQayg5mZlRsq_Zg&oe=63FE618B&_nc_sid=8fd12b"
                },
                
                ...
                
            ],
            "relatedAccounts": [
                {
                    "username": "houseofhighlights",
                    "name": "House of Highlights",
                    "verified": false
                },
                {
                    "username": "sportscenter",
                    "name": "SportsCenter",
                    "verified": false
                },
                
                ...
            ]
        },
        "errors": [],
        "status_code": 12000
    },
    "task_id": "7034884446637549569",
    "url": "https://www.instagram.com/nba"
}
        
```
### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramprofile.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramprofile.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramprofile.py > instagramprofile.py ``` |
| PHP                 | [php/instagramprofile.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramprofile.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramprofile.php > instagramprofile.php  ``` |
| Node.js                 | [nodejs/instagramprofile.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramprofile.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramprofile.js > instagramprofile.js ``` |


### Instagram GraphQL profile

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/nba)
```target``` (in this example, instagram_graphql_profile)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram profile URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramgraphqlprofile.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlprofile.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlprofile.py > instagramgraphqlprofile.py ``` |
| PHP                 | [php/instagramgraphqlprofile.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlprofile.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlprofile.php > instagramgraphqlprofile.php  ``` |
| Node.js                 | [nodejs/instagramgraphqlprofile.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlprofile.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlprofile.js > instagramgraphqlprofile.js ``` |

### Instagram post

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```
Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/p/ChYHpdAvnob/)
```target``` (in this example, instagram_post)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram post URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagrampost.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagrampost.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagrampost.py > instagrampost.py ``` |
| PHP                 | [php/instagrampost.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagrampost.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagrampost.php > instagrampost.php  ``` |
| Node.js                 | [nodejs/instagrampost.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagrampost.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagrampost.js > instagrampost.js ``` |

### Instagram GraphQL post

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```
Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/p/ChYHpdAvnob/)
```target``` (in this example, instagram_graphql_post)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram post URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramgraphqlpost.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlpost.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlpost.py > instagramgraphqlpost.py ``` |
| PHP                 | [php/instagramgraphqlpost.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlpost.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlpost.php > instagramgraphqlpost.php  ``` |
| Node.js                 | [nodejs/instagramgraphqlpost.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlpost.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlpost.js > instagramgraphqlpost.js ``` |

### Instagram reel

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/reel/ClfPAdQgqTc/)
```target``` (in this example, instagram_reel)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram reel URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramreel.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramreel.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramreel.py > instagramreel.py ``` |
| PHP                 | [php/instagramreel.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramreel.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramreel.php > instagramreel.php  ``` |
| Node.js                 | [nodejs/instagramreel.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramreel.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramreel.js > instagramreel.js ``` |


### Instagram GraphQL hashtag

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/explore/tags/nba/)
```target``` (in this example, instagram_graphql_hashtag)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram hashtag URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramgraphqlhashtag.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlhashtag.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlhashtag.py > instagramgraphqlhashtag.py ``` |
| PHP                 | [php/instagramgraphqlhashtag.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlhashtag.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlhashtag.php > instagramgraphqlhashtag.php  ``` |
| Node.js                 | [nodejs/instagramgraphqlhashtag.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlhashtag.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlhashtag.js > instagramgraphqlhashtag.js ``` |

### Create callback for Instagram post

API Link: https://scraper-api.smartproxy.com/v2/task

```http
  POST /task
```
Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/p/ChYHpdAvnob/)
```target``` (in this example, instagram_post)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram post URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramcallback.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramcallback.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramcallback.py > instagramcallback.py ``` |
| PHP                 | [php/instagramcallback.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramcallback.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramcallback.php > instagramcallback.php  ``` |
| Node.js                 | [nodejs/instagramcallback.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramcallback.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramcallback.js > instagramcallback.js ``` |

### Retrieve parsed results via callback

API Link: https://scraper-api.smartproxy.com/v2/task/{Task_ID}/results?type=parsed

```http
  GET /task/{{Task ID}}/results?type=parsed
```

### Retrieve raw HTML results via callback

API Link: https://scraper-api.smartproxy.com/v2/task/{Task_ID}/results?type=raw

```http
  GET /task/{{Task ID}}/results?type=raw
```

## TikTok


### TikTok API Profile

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.tiktok.com/@nba)
```target``` (in this example, tiktok_profile)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  TikTok profile URL |
| `target` | `string` |  target  |
| `count` | `integer` |  Number of results to be returned.
At least 1. At most 35. Defaults to 10.  |
| `timestamp` | `integer` |  UNIX timestamp, Given a timestamp date, the last count entries will be returned, starting from that date.
Timestamp must be in seconds format (this will generally be 10 digits long)  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/tiktokapiprofile.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokapiprofile.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokapiprofile.py > tiktokapiprofile.py ``` |
| PHP                 | [php/tiktokapiprofile.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokapiprofile.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokapiprofile.php > tiktokapiprofile.php  ``` |
| Node.js                 | [nodejs/tiktokapiprofile.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokapiprofile.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokapiprofile.js > tiktokapiprofile.js ``` |

### TikTok profile

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.tiktok.com/@nba)
```target``` (in this example, tiktok_profile)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  TikTok profile URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/tiktokprofile.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokprofile.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokprofile.py > tiktokprofile.py ``` |
| PHP                 | [php/tiktokprofile.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokprofile.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokprofile.php > tiktokprofile.php  ``` |
| Node.js                 | [nodejs/tiktokprofile.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokprofile.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokprofile.js > tiktokprofile.js ``` |



### TikTok post

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.tiktok.com/@nba/video/7196793231042989354)
```target``` (in this example, tiktok_post)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  TikTok post URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |


### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/tiktokpost.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokpost.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokpost.py > tiktokpost.py ``` |
| PHP                 | [php/tiktokpost.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokpost.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokpost.php > tiktokpost.php  ``` |
| Node.js                 | [nodejs/tiktokpost.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokpost.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokpost.js > tiktokpost.js ``` |

### TikTok API hashtag

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```query``` (in this example, tasty)
```target``` (in this example, tiktok_api_hashtag)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  TikTok hashtag query |
| `target` | `string` |  target  |
| `count` | `integer` |  Returns the most recent count results.
At least 1. At most 35. Defaults to 10.  |
| `cursor` | `integer` |  Number for indicating how offset the results should be. Defaults to 0 (fetches results that you would see at the top of the page)	  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/tiktokapihashtag.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokapihashtag.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokapihashtag.py > tiktokapihashtag.py ``` |
| PHP                 | [php/tiktokapihashtag.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokapihashtag.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokapihashtag.php > tiktokapihashtag.php  ``` |
| Node.js                 | [nodejs/tiktokapihashtag.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokapihashtag.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokapihashtag.js > tiktokapihashtag.js ``` |

### TikTok hashtag

API Link: https://scraper-api.smartproxy.com/v2/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.tiktok.com/tag/satisfying)
```target``` (in this example, tiktok_hashtag)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  TikTok hashtag URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |


### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/tiktokhashtag.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokhashtag.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/tiktokhashtag.py > tiktokhashtag.py ``` |
| PHP                 | [php/tiktokhashtag.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokhashtag.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/tiktokhashtag.php > tiktokhashtag.php  ``` |
| Node.js                 | [nodejs/tiktokhashtag.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokhashtag.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/tiktokhashtag.js > tiktokhashtag.js ``` |

## Targets

### List of supported targets for the 'target' parameter
```
instagram_post
instagram_profile
instagram_reel
instagram_graphql_post
instagram_graphql_profile
instagram_graphql_hashtag
tiktok_profile
tiktok_api_profile
tiktok_post
tiktok_hashtag
tiktok_api_hashtag
twitter_user
twitter_user_tweets
twitter_user_liked_tweets
twitter_search
```

## Parameters

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Social Media URL |
| `query` | `string` |  Request query |
| `count` | `integer` |  Result Count |
| `cursor` | `integer` |  Number for indicating how offset the results should be. Defaults to 0 (fetches results that you would see at the top of the page)	  |
| `timestamp` | `integer` |  UNIX timestamp, Given a timestamp date, the last count entries will be returned, starting from that date.
Timestamp must be in seconds format (this will generally be 10 digits long)  |
| `target` | `string` |  Desired target |
| `locale` | `string` |  Language Locale  |
| `geo` | `string` | Geolocation  |


### HTTP Response Codes

| Response | Description     | Solution                |
| :-------- | :------- | :------------------------- |
| **200** - Success | Server has replied and given requested response.	 | Celebrate! |
| **204** - No content | Job not completed yet. | Wait a few seconds before trying again. |
| **400** - Multiple error messages | Bad structure of the request. | Re-check your request to make sure it is in the correct format. |
| **401** - Invalid / not provided authorization header (client not found) | Incorrect login credentials or missing authorization. | Re-check your provided credentials for authorization. |
| **403** - Forbidden | Your account does not have access to this resource. | Make sure the target is supported by us |
| **404** - Not found | Your target was not found. | Re-check your targeted URL. |
| **429** - Too many requests | Exceeded rate limit for your subscription. | Make sure you still have at least one request left. Wait a couple minutes and try again. If you are encountering the error often – chat with us to see if your rate limit can be increased. |
| **500** - Internal error | Service unavailable, possibly due to some issues we are encountering. | Wait a couple minutes and send another request. Contact us for more information. |
| **524** - Timeout | Service unavailable, possibly due to some issues we are encountering. | Wait a couple minutes and send another request. Contact us for more information. |

### Parsed Result Response Codes

| Response | Description |
| :-------- | :------- | 
| **12000** - Success | Server has replied and given the requested response. |
| **12002** - Error | Parsing has failed completely. |
| **12003** - Not supported | Targeted website parsing is not supported. |
| **12004** - Response not full | Some fields were not parsed and are missing. |
| **12005** - Response not fully parsed | Some fields might not have been parsed and are returned unparsed. |
| **12006** - Error | Unexpected error. Let us know the task ID and we will check what went wrong. |
| **12007** - Unknown | We could not determine whether the data was parsed correctly. |
| **12008** - Error | Failed to parse all the data. |
| **12009** - Error | Target not found. Make sure the parameters you passed are correct and supported. |

## Postman Collection

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/23304112-98896147-a3b4-48fd-93f5-accd15020b60?action=collection%2Ffork&collection-url=entityId%3D23304112-98896147-a3b4-48fd-93f5-accd15020b60%26entityType%3Dcollection%26workspaceId%3D52705bab-433c-4fbf-afce-ccbfc97430fe)

## License
 
All code is released under [MIT License](https://github.com/Smartproxy/Smartproxy/blob/master/LICENSE)
