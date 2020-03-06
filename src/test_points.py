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
    testData ='{"groups":[{"group_status":0,"is_primary":true,"id":2244,"name":"С2712_5"}],"student_id":16543,"current_group_id":2244,"full_name":"Кисіль Олег Васильович","achieves_count":11,"stream_id":24,"stream_name":"МКА2017","group_name":"С2712_5","level":4,"photo":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XKRpO91ZfYWESaSSTCnFW9HxMcByqbxbZslluHLOv2Mk%3D","gaming_points":[{"new_gaming_point_types__id":1,"points":478},{"new_gaming_point_types__id":2,"points":804}],"spent_gaming_points":[{"new_gaming_point_types__id":1,"points":230},{"new_gaming_point_types__id":2,"points":360}],"visibility":{"is_design":false,"is_vacancy":false,"is_signal":true,"is_promo":false,"is_test":false,"is_email_verified":true,"is_quizzes_expired":false,"is_debtor":false,"is_phone_verified":true,"is_only_profile":false}}'
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the text property
    def mock_get(*args, **kwargs):
        return MockResponse(testData)

    # apply the monkeypatch for requests.post to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # API.getkey that using patched requests.post
    result = API.GetPoints('test')
    print(result)
    assert result == [478,804,478+804]