# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import requests

import API

# custom class to be the mock return value
# will mock return from requests.post()
class MockResponse:
    def __init__(self,response): 
        self.text = response

def test_get_json(monkeypatch):
    # test raw JSON input
    testData ='[{"counter_type":1,"counter":107},{"counter_type":3,"counter":0},{"counter_type":0,"counter":3},{"counter_type":2,"counter":0},{"counter_type":5,"counter":0},{"counter_type":4,"counter":110}]'
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the text property
    def mock_get(*args, **kwargs):
        return MockResponse(testData)

    # apply the monkeypatch for requests.post to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # API.getkey that using patched requests.post
    result = API.GetHomeworks('test')
    assert result == [110, 107, 3, 0, 0]