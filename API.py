import requests
import json
import sys


#validate parsed JSON data from MyStat
def validate (data):
        try: # Yeah I can`t do it without catching some error (P.S. somehow doesn`t working for GET with auth)
            error = data[0]['message']
            raise Exception('Error from MyStat ! ' + error)
        except KeyError as e:
            return data

def GetWithHeader (token,url,data=''):
    response = requests.get(url, data = data, headers={"authorization":"Bearer "+token})
    response = json.loads(response.text)
    return validate(response)

def PostWithHeader (token,url,data):
    response = requests.post(url, data = data, headers={"authorization":"Bearer "+token})
    response = json.loads(response.text)
    return validate(response)

#make response validate for any errors and return parsed JSON 
def Post (data,url):
    response = requests.post(url, data = data)
    response = json.loads(response.text)
    return validate(response)



def getKey (password,username):
    url = 'https://msapi.itstep.org/api/v2/auth/login'
    myobj = {'application_key': '6a56a5df2667e65aab73ce76d1dd737f7d1faef9c52e8b8c55ac75f565d8e8a6',
             'id_city':31 ,
             'username':username,
             'password':password
            }
    return Post(myobj,url)['access_token']

def GetUserData(token):
    url = 'https://msapi.itstep.org/api/v2/settings/user-info'
    return GetWithHeader(token,url)

def GetStreamLeaderboard(token):
    url ="https://msapi.itstep.org/api/v2/dashboard/progress/leader-stream"
    return GetWithHeader(token,url)

def GetClassLeaderboard(token):
    url ="https://msapi.itstep.org/api/v2/dashboard/progress/leader-group"
    return GetWithHeader(token,url)



