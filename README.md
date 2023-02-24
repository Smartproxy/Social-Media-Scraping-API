
# Social Media Scraping API

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
https://scraper-api.smartproxy.com/v1/scrape
```

### Asynchronous (create a callback)

```http
POST
https://scraper-api.smartproxy.com/v1/task
```

### Asynchronous (receive data in raw HTML)

```http
GET
https://scraper-api.smartproxy.com/v1/task/{{task_id}}/results?type=raw
```

### Asynchronous (receive data parsed in JSON)

```http
GET
https://scraper-api.smartproxy.com/v1/task/{{task_id}}/results?type=Parsed
```

## Instagram

Instagram can be targeted using direct URL.

The `instagram_post`, `instagram_profile`, and `instagram_reel` targets allow you to scrape Instagram's HTML and receive data parsed in JSON.

The `instagram_graphql_post`, `instagram_graphql_profile`, `instagram_graphql_reel`, and `instagram_graphql_hashtag` target allows you to scrape Instagram's GraphQL API endpoint and receive data parsed in JSON.

### Instagram profile

API Link: https://scraper-api.smartproxy.com/v1/scrape

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
                {
                    "href": "https://www.instagram.com/p/CpCGhbfM3wI/",
                    "description": "👀 all the angles of @joelembiid’s BIG BLOCK!",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332786084_1841561139556840_6064534978102120688_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=4BdjNRsOM_UAX8snSar&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfC3l8sLsAVXaMEvoDi3Xn3IhIctgpTiZIH6zr64xES3Jw&oe=63FCBB1C&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCGPbJrsNu/",
                    "description": "@kidkessler comes big for the @utahjazz on both ends in clutch! #NBARooks",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332937720_1336070493900722_3242030842850361447_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=b-aISolenUoAX-v37vZ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCTYoqeaIsKIe9nFGBBUdaGEyGvr6qzxqdUSx1ra_DhzA&oe=63FA6351&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpB6IrmgTTA/",
                    "description": "What a sequence for the @sixers!",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332730248_1018336802887989_7073365282672589919_n.jpg?stp=c0.237.608.608a_dst-jpg_e15&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=_-JTaye6m00AX9i4goX&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCPXuGIaMGuZ9bI_yTsumqh9JkehB4T1A4D-8hK2Seikg&oe=63FA371C&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCE_JrrS3g/",
                    "description": "@badbunnypr on the move! #NBACelebRow",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332475346_1707400709694743_8751817164031140951_n.jpg?stp=c0.113.1440.1440a_dst-jpg_e35_s640x640_sh0.08&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=Rxir8wUoO6kAX9GG88Y&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfA3u7IdJI-qao5dhycieh0_8vCCHVt8MPZhMcHzcBrNFA&oe=63FE0CB7&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCEng0LZ4i/",
                    "description": "💎 @saweetie in LA! 😍#NBACelebRow",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332466247_575939754589805_3880917861593240283_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=9TVp6rt4-68AX9a8ual&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDtY_HiNLHqxchtjYJBFhQ_7jzUc5f9D6JYovC-hRQiSw&oe=63FE1E7E&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCBAqhgVcI/",
                    "description": "@laurimarkkanen ATTACKS the rim! 💥",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332351148_570292721719726_7546698225621933573_n.jpg?stp=c0.237.608.608a_dst-jpg_e15&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=DfsmqqRl_t8AX89sAKE&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfByS40EMkjy5lDk64tNkm1ekWr-Jrw7MBNFPZTRXUQJJQ&oe=63FAAC83&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCB76lrFSq/",
                    "description": "would run through a brick wall for him 🫡\n\n#TakeNote",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332360842_1231324224142201_2320874905033815002_n.jpg?stp=c0.237.608.608a_dst-jpg_e15&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=yNqMn2R0yTwAX8rgXh8&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBCHGf1KUxzNaBgCAesz3YsxktPOCglTkgV2SmG4wbNHQ&oe=63FA1B0E&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpCBOMRDG73/",
                    "description": "slomo shae 🎥",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332338371_221793603588279_1862268358417244269_n.jpg?stp=c0.280.720.720a_dst-jpg_e15_s640x640&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=VyM-kbRf5cgAX-A8LKJ&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBoElJcCP379GvZyZNr3Fk6chxPmYiiOLMQlm_s3ob94Q&oe=63FA64EF&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpB-FFxtUDD/",
                    "description": "THIRTY-EIGHT",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332682642_513369970981452_7479635896081670345_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=1c2b13aTTT8AX_CVoGY&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfAfr3YK4VR_mpRhLwDkkqj2evmdqX9hhpwbYrSrJ8YGpg&oe=63FD3FA7&_nc_sid=8fd12b"
                },
                {
                    "href": "https://www.instagram.com/p/CpB9uZxAtxL/",
                    "description": "@kingjames rocks the rim off the @ds17_fg dime!! \n\n@lakers • @nbaontnt",
                    "image": "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/332345406_194249613291132_7248645503716906115_n.jpg?stp=c0.237.608.608a_dst-jpg_e15&_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=1&_nc_ohc=XKultlNX08IAX_g_GAL&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfAoNLj-6_6npXl4VsOsyxP-Drd1mSai6QLPsGNoMyN30A&oe=63FA7ADF&_nc_sid=8fd12b"
                }
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
                {
                    "username": "shaq",
                    "name": "DR. SHAQUILLE O'NEAL Ed.D.",
                    "verified": false
                },
                {
                    "username": "kyrieirving",
                    "name": "Hélà",
                    "verified": false
                },
                {
                    "username": "jamorant",
                    "name": "12 💙",
                    "verified": false
                },
                {
                    "username": "nbahistory",
                    "name": "NBA History",
                    "verified": false
                },
                {
                    "username": "433",
                    "name": "433",
                    "verified": false
                },
                {
                    "username": "jaytatum0",
                    "name": "Jayson Tatum🙏🏀",
                    "verified": false
                },
                {
                    "username": "dallasmavs",
                    "name": "Dallas Mavericks",
                    "verified": false
                },
                {
                    "username": "slam",
                    "name": "SLAM",
                    "verified": false
                },
                {
                    "username": "nikebasketball",
                    "name": "Nike Basketball",
                    "verified": false
                },
                {
                    "username": "premierleague",
                    "name": "Premier League",
                    "verified": false
                },
                {
                    "username": "ufc",
                    "name": "UFC",
                    "verified": false
                },
                {
                    "username": "suns",
                    "name": "Phoenix Suns",
                    "verified": false
                },
                {
                    "username": "memgrizz",
                    "name": "Memphis Grizzlies",
                    "verified": false
                },
                {
                    "username": "neymarjr",
                    "name": "NJ 🇧🇷",
                    "verified": false
                },
                {
                    "username": "fiba",
                    "name": "FIBA",
                    "verified": false
                },
                {
                    "username": "fcbarcelona",
                    "name": "FC Barcelona",
                    "verified": false
                },
                {
                    "username": "jumpman23",
                    "name": "Jordan",
                    "verified": false
                },
                {
                    "username": "cavs",
                    "name": "Cleveland Cavaliers",
                    "verified": false
                },
                {
                    "username": "fabriziorom",
                    "name": "Fabrizio Romano",
                    "verified": false
                },
                {
                    "username": "tristanj22",
                    "name": "Tristan Jass",
                    "verified": false
                },
                {
                    "username": "21savage",
                    "name": "",
                    "verified": false
                },
                {
                    "username": "brfootball",
                    "name": "Bleacher Report Football",
                    "verified": false
                },
                {
                    "username": "50cent",
                    "name": "50 Cent",
                    "verified": false
                },
                {
                    "username": "sixers",
                    "name": "Philadelphia 76ers",
                    "verified": false
                },
                {
                    "username": "nbalatam",
                    "name": "NBA Latam",
                    "verified": false
                },
                {
                    "username": "trailblazers",
                    "name": "Portland Trail Blazers",
                    "verified": false
                },
                {
                    "username": "joelembiid",
                    "name": "Joel \"The Process\" Embiid",
                    "verified": false
                },
                {
                    "username": "mancity",
                    "name": "Manchester City",
                    "verified": false
                },
                {
                    "username": "funnyhoodvidz",
                    "name": "FunnyHoodVidz",
                    "verified": false
                },
                {
                    "username": "nbabrasil",
                    "name": "NBA Brasil",
                    "verified": false
                },
                {
                    "username": "houstonrockets",
                    "name": "Houston Rockets",
                    "verified": false
                },
                {
                    "username": "fchwpo",
                    "name": "Jaylen Brown",
                    "verified": false
                },
                {
                    "username": "supremedreams_1",
                    "name": "Mark Phillips",
                    "verified": false
                },
                {
                    "username": "fcbayern",
                    "name": "FC Bayern",
                    "verified": false
                },
                {
                    "username": "hoodclips",
                    "name": "HoodClips",
                    "verified": false
                },
                {
                    "username": "chelseafc",
                    "name": "Chelsea FC",
                    "verified": false
                },
                {
                    "username": "deestroying",
                    "name": "Dee",
                    "verified": false
                },
                {
                    "username": "kodakblack",
                    "name": "Kutthroat Bill",
                    "verified": false
                },
                {
                    "username": "vindiesel",
                    "name": "Vin Diesel",
                    "verified": false
                },
                {
                    "username": "offsetyrn",
                    "name": "OFFSET",
                    "verified": false
                },
                {
                    "username": "nuggets",
                    "name": "Denver Nuggets",
                    "verified": false
                },
                {
                    "username": "playboicarti",
                    "name": "",
                    "verified": false
                },
                {
                    "username": "sidemen",
                    "name": "Sidemen",
                    "verified": false
                },
                {
                    "username": "lilyachty",
                    "name": "C.V T",
                    "verified": false
                },
                {
                    "username": "hypebeast",
                    "name": "HYPEBEAST",
                    "verified": false
                },
                {
                    "username": "hurdles",
                    "name": "Sports Videos",
                    "verified": false
                },
                {
                    "username": "k.mbappe",
                    "name": "Kylian Mbappé",
                    "verified": false
                },
                {
                    "username": "shamsnba",
                    "name": "Shams Charania",
                    "verified": false
                },
                {
                    "username": "hoopsnation",
                    "name": "Hoops Nation",
                    "verified": false
                },
                {
                    "username": "paolo5",
                    "name": "Paolo Banchero🇮🇹",
                    "verified": false
                },
                {
                    "username": "nbaeurope",
                    "name": "NBA Europe",
                    "verified": false
                },
                {
                    "username": "orlandomagic",
                    "name": "Orlando Magic",
                    "verified": false
                },
                {
                    "username": "stephenasmith",
                    "name": "Stephen A. Smith",
                    "verified": false
                },
                {
                    "username": "jalen",
                    "name": "Jalen Green",
                    "verified": false
                },
                {
                    "username": "magicjohnson",
                    "name": "Earvin \"Magic\" Johnson",
                    "verified": false
                },
                {
                    "username": "overtimeszn",
                    "name": "Overtime SZN",
                    "verified": false
                },
                {
                    "username": "dunk",
                    "name": "dunk.",
                    "verified": false
                },
                {
                    "username": "famouslos32",
                    "name": "famouslos32",
                    "verified": false
                },
                {
                    "username": "pacers",
                    "name": "Indiana Pacers",
                    "verified": false
                },
                {
                    "username": "usabasketball",
                    "name": "USA Basketball",
                    "verified": false
                },
                {
                    "username": "euroleague",
                    "name": "Turkish Airlines EuroLeague",
                    "verified": false
                },
                {
                    "username": "djkhaled",
                    "name": "DJ KHALED",
                    "verified": false
                },
                {
                    "username": "leaguealerts",
                    "name": "LeagueAlerts Inc.",
                    "verified": false
                },
                {
                    "username": "garydwayne",
                    "name": "GPII",
                    "verified": false
                },
                {
                    "username": "bball",
                    "name": "BBALL",
                    "verified": false
                },
                {
                    "username": "nflonfox",
                    "name": "NFL on FOX",
                    "verified": false
                },
                {
                    "username": "karimbenzema",
                    "name": "Karim Benzema",
                    "verified": false
                },
                {
                    "username": "jordanclarksons",
                    "name": "",
                    "verified": false
                },
                {
                    "username": "eamaddennfl",
                    "name": "EA SPORTS Madden NFL 23",
                    "verified": false
                },
                {
                    "username": "tacotuuesday",
                    "name": "Taco Tuesday",
                    "verified": false
                },
                {
                    "username": "kimkardashian",
                    "name": "Kim Kardashian",
                    "verified": false
                },
                {
                    "username": "9gag",
                    "name": "9GAG: Go Fun The World",
                    "verified": false
                },
                {
                    "username": "judebellingham",
                    "name": "Jude Bellingham",
                    "verified": false
                },
                {
                    "username": "milliebobbybrown",
                    "name": "Millie Bobby Brown",
                    "verified": false
                },
                {
                    "username": "arsenal",
                    "name": "Arsenal",
                    "verified": false
                },
                {
                    "username": "basketball",
                    "name": "BASKETBALL",
                    "verified": false
                },
                {
                    "username": "juventus",
                    "name": "Juventus",
                    "verified": false
                },
                {
                    "username": "antonelaroccuzzo",
                    "name": "Antonela Roccuzzo",
                    "verified": false
                }
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

API Link: https://scraper-api.smartproxy.com/v1/scrape

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

API Link: https://scraper-api.smartproxy.com/v1/scrape

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

API Link: https://scraper-api.smartproxy.com/v1/scrape

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

API Link: https://scraper-api.smartproxy.com/v1/scrape

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

### Instagram GraphQL reel

API Link: https://scraper-api.smartproxy.com/v1/scrape

```http
  POST /scrape
```

Payload type: JSON

Required parameters: 
```url``` (in this example, https://www.instagram.com/reel/ClfPAdQgqTc/)
```target``` (in this example, instagram_graphql_reel)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Instagram reel URL |
| `target` | `string` |  target  |
| `locale` | `string` |  language locale  |
| `geo` | `string` | geolocation  |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/instagramgraphqlreel.py](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlreel.py) |``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/python/instagramgraphqlreel.py > instagramgraphqlreel.py ``` |
| PHP                 | [php/instagramgraphqlreel.php](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlreel.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/php/instagramgraphqlreel.php > instagramgraphqlreel.php  ``` |
| Node.js                 | [nodejs/instagramgraphqlreel.js](https://github.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlreel.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/Social-Media-Scraping-API/blob/main/nodejs/instagramgraphqlreel.js > instagramgraphqlreel.js ``` |


### Instagram GraphQL hashtag

API Link: https://scraper-api.smartproxy.com/v1/scrape

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

API Link: https://scraper-api.smartproxy.com/v1/task

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

API Link: https://scraper-api.smartproxy.com/v1/task/{Task_ID}/results?type=parsed

```http
  GET /task/{{Task ID}}/results?type=parsed
```

### Retrieve raw HTML results via callback

API Link: https://scraper-api.smartproxy.com/v1/task/{Task_ID}/results?type=raw

```http
  GET /task/{{Task ID}}/results?type=raw
```

## TikTok

### TikTok profile

API Link: https://scraper-api.smartproxy.com/v1/scrape

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



## TikTok post

API Link: https://scraper-api.smartproxy.com/v1/scrape

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


## Targets

### List of supported targets for the 'target' parameter
```
instagram_post
instagram_profile
instagram_reel
instagram_graphql_post
instagram_graphql_profile
instagram_graphql_reel
instagram_graphql_hashtag
tiktok_profile
tiktok_post
```

## Parameters

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Social Media URL |
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

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/23304112-92a123e7-171c-497e-8ca1-57eff04361f3?action=collection%2Ffork&collection-url=entityId%3D23304112-92a123e7-171c-497e-8ca1-57eff04361f3%26entityType%3Dcollection%26workspaceId%3D52705bab-433c-4fbf-afce-ccbfc97430fe)


## License

All code is released under [MIT License](https://github.com/Smartproxy/Smartproxy/blob/master/LICENSE)
