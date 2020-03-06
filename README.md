# Python API for [MyStat](https://mystat.itstep.org/ru/auth/login/index) [![Build Status](https://travis-ci.com/Nereg/MyStatAPI.svg?branch=master)](https://travis-ci.com/Nereg/MyStatAPI) [![CodeFactor](https://www.codefactor.io/repository/github/nereg/mystatapi/badge/master)](https://www.codefactor.io/repository/github/nereg/mystatapi/overview/master)
## Сapability
* Login with password and login 
* Full user info (like full name, photo url, group name, level and more)
* Two leaderboards:
  * Stream leaderboard (each with photo url + count of points)
  * Group leaderboard (photo url and also points)
* Get count of all three types of points (crystals, coins and stars)
* Future exams
* Can refresh access token
## Todo 
- [ ] Homeworks (for now read only)
## How to install
Just copy API.py from [src](/src) directory to your project and import.
Yeah it isn't a PyPi package now.
## How to run auto tests
- Clone or download this repository 
- Go in downloaded directory 
- `pip install -r requirements.txt`
- `pytest src/`
Also if you have MyStat account you can run [test.example.py](/test.example.py)
Just paste your username and password
# This repository using GNU GPLv3 [license](/LICENSE) 
