# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import requests,json,pytest

import API

def test_first():
    with pytest.raises(Exception): 
        test_data = json.loads('[{"field":"username","message":"This is test!"}]')
        API.validate(test_data)

def test_second(): #tests randoms JSOn with no error in it 
    test_data = json.loads('{"totalCount":null,"Just random JSON!":3,"weekDiff":0,"monthDiff":0}')
    result = API.validate(test_data)
    assert result == test_data

def test_third(): # tests empty JSON
    test_data = json.loads('[]')
    result = API.validate(test_data)
    assert result == test_data