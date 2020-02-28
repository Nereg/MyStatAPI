import requests
import json
import sys



# Validate parsed JSON data from MyStat
# If any error (in JSON message) it will raise it
def validate (data):
        try: # Yeah I can`t do it without catching some error (P.S. somehow doesn`t working for GET with auth)
            error = data[0]['message']
            raise Exception(error)
        except KeyError:
            return data
        except IndexError: # if data is [] (empty JSON)
            return data

def GetWithHeader (token,url,data=''): # get with AUTH header
    response = requests.get(url, data = data, headers={"authorization":"Bearer "+token}) #make get request with data and auth header
    response = json.loads(response.text) # parse JSON
    return validate(response) # validate and return 

def PostWithHeader (token,url,data): # POST request with auth header
    response = requests.post(url, data = data, headers={"authorization":"Bearer "+token})# create POST request with data and auth token
    response = json.loads(response.text) # parse JSON
    return validate(response) # validate and return

def Post (data,url,headers={}): # POST request with custom headers
    response = requests.post(url, data = data,headers=headers) # create POST request with data and custom content
    response = json.loads(response.text) # parse JSON
    return validate(response) # validate and return 

def Get (data,url,headers={}): # GET request with custom headers
    response = requests.get(url, data = data) # create GET request with data and custom content
    response = json.loads(response.text) # parse JSON
    return validate(response) # validate and return 

def getKey (password,username):
    """Get access and refresh tokens from password and username

    Return : list 
    Format : [access_token,refresh_token]
    """
    url = 'https://msapi.itstep.org/api/v2/auth/login'
    myobj = {'application_key': '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6',
             'id_city':31 , # my dear city KHERSON P.S In new version of API it doesn't matter which id I think
             'username':username,
             'password':password
            }
    result = Post(myobj,url)
    return [result['access_token'],result['refresh_token']]

def getRefreshTime(password,username):
    """Get time when access and refresh token expires

    Return : list
    Format : [access_refresh_time,refresh_token_time]
    """
    url = 'https://msapi.itstep.org/api/v2/auth/login'
    myobj = {'application_key': '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6',
             'id_city':31 ,
             'username':username,
             'password':password
            }
    result = Post(myobj,url)
    access_refresh_time = result['expires_in_access']
    refresh_token_time = result['expires_in_refresh']
    return [access_refresh_time,refresh_token_time] #just UNIX timestamps 

def GetUserData(token):
    """Get data of user from MyStat

    Return : Array (parsed JSON)
    Format : complex (see doc)
    """
    url = 'https://msapi.itstep.org/api/v2/settings/user-info'
    return GetWithHeader(token,url)

def GetStreamLeaderboard(token):
    """Get stream leaderboard for user from Mystat

    Return : Array (parsed JSON)
    Format : complex (see doc)
    """
    url ="https://msapi.itstep.org/api/v2/dashboard/progress/leader-stream"
    return GetWithHeader(token,url)

def GetClassLeaderboard(token):
    """Get class leaderboard for user from Mystat
    
    Return : Array (parsed JSON)
    Format : complex (see doc)
    """
    url ="https://msapi.itstep.org/api/v2/dashboard/progress/leader-group"
    return GetWithHeader(token,url)

def GetPoints(token):
    """Get number of stars,coins and crystals of user
    
    Return : List
    Format : [Crystals,Coins,Stars]
    """
    points = GetUserData(token)
    points = points['gaming_points']
    data = [points[0]['points'] , points[1]['points'] , points[0]['points'] + points[1]['points']]
    return data

def GetHomeworks(token):
    """Get number of homeworks for user
    
    Return : List
    Format : [All,Done,Overdue,Current,OnReview]
    """
    url = 'https://msapi.itstep.org/api/v2/count/homework'
    get = GetWithHeader(token,url)
    all = get[5]['counter']
    done = get[0]['counter']
    overdue = get[2]['counter']
    current = get[1]['counter'] # I took position from old code so it may be wrong
    review = get[3]['counter']
    data = [all,done,overdue,current,review]
    return data

def GetFutureExsams(token):
    url = 'https://msapi.itstep.org/api/v2/dashboard/info/future-exams'
    get = GetWithHeader(token,url)
    return get

def RefreshToken(refresh_token):
    """Get new access and refresh token from refresh token
    
    Return : List
    Format : [access_token,refresh_token]
    """
    data = json.dumps({"refresh_token":refresh_token})
    url = "https://msapi.itstep.org/api/v2/auth/refresh"
    result = Post(data,url,{'content-type': 'application/json'})
    return [result['access_token'],result['refresh_token']]

    