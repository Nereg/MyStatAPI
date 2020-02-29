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
    testData = '{"access_token":"0K6gn6i16dD43-7hgBaO-ns0tkNyNjhHijYAvnAzhkJFT91Dl1wwWJYQNFKXrs5B","refresh_token":"ifvRfjRlrF0KAV8K-TmDLcTqDfhhkb_M_Wl67EirJg9YTaAJ2OXXeCmm1rlb18bE","expires_in_refresh":1582030140,"expires_in_access":1581860940,"user_type":1,"upload_credentials":null,"city_data":null}'
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the text property
    def mock_get(*args, **kwargs):
        return MockResponse(testData)

    # apply the monkeypatch for requests.post to mock_get
    monkeypatch.setattr(requests, "post", mock_get)

    # API.getkey that using patched requests.post
    result = API.getKey('test','test')
    assert result == ['0K6gn6i16dD43-7hgBaO-ns0tkNyNjhHijYAvnAzhkJFT91Dl1wwWJYQNFKXrs5B','ifvRfjRlrF0KAV8K-TmDLcTqDfhhkb_M_Wl67EirJg9YTaAJ2OXXeCmm1rlb18bE']