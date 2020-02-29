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
    testData = '{"access_token":"LUz3QvJzrz1Xk_vfBFJ401BX3S7zVQ-XZZ3HXtpG9Z15Dau9aswnI-qh-bqbAz_V","refresh_token":"LoH9kzUnOdK02nAPIu8crgeYXMNq0xvI_PrxckAHn4AvOX9vHYogLaQ8h36QU95n","expires_in_refresh":1581939935,"expires_in_access":1581770735,"user_type":1,"upload_credentials":{"env":"prod","upload_token":"LUz3QvJzrz1Xk_vfBFJ401BX3S7zVQ-XZZ3HXtpG9Z15Dau9aswnI-qh-bqbAz_V","url":"https://mystatfiles.itstep.org/index.php"},"city_data":{"id_city":31,"prefix":"kherson","translate_key":"KHERSON","timezone_name":"Europe/Kiev","country_code":"UA/UKR","market_status":1,"name":"Херсон"}}'
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the text property
    def mock_get(*args, **kwargs):
        return MockResponse(testData)

    # apply the monkeypatch for requests.post to mock_get
    monkeypatch.setattr(requests, "post", mock_get)

    # API.getkey that using patched requests.post
    result = API.getKey('test','test')
    assert result == ['LUz3QvJzrz1Xk_vfBFJ401BX3S7zVQ-XZZ3HXtpG9Z15Dau9aswnI-qh-bqbAz_V','LoH9kzUnOdK02nAPIu8crgeYXMNq0xvI_PrxckAHn4AvOX9vHYogLaQ8h36QU95n']