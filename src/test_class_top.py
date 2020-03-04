# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import requests,json

import API

# custom class to be the mock return value
# will mock return from requests.post()
class MockResponse:
    def __init__(self,response): 
        self.text = response

def test_get_json(monkeypatch):
    # test raw JSON input
    testData = '[{"amount":1251,"id":16543,"full_name":"Кисіль Олег Васильович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XKRpO91ZfYWESaSSTCnFW9HxMcByqbxbZslluHLOv2Mk%3D","position":1},{"amount":1099,"id":16575,"full_name":"Савченко Романна Геннадіївна","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XtdSUz018WmWZUBR0FFzB1iiCUQzisxpXI7Jo6N%2FNToU%3D","position":2},{"amount":1017,"id":16518,"full_name":"Нещерецький Арсеній Сергійович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XIktB1q%2B58YTyY8VTnyYf0GhSlPJhsxjpzHc5hOVnrcE%3D","position":3},{"amount":987,"id":16576,"full_name":"Якубенко Богдан Андрійович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XQPzZXL4kp%2Bifq0S9NJw6wApdN1SE40GYSI%2FUQMcMoic%3D","position":4},{"amount":981,"id":16448,"full_name":"Фудоров Дмитро Геннадійович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XVsOGs2AVLtFi%2BfJettvqJ9ZCxvrJG2hZaVgbponFZrc%3D","position":5},{"amount":965,"id":16517,"full_name":"Островський Лев Едуардович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0X32%2BSKV60sKdY4fpVdmm%2BKP%2FzkUQInA%2FfaS73lXLGeT4%3D","position":6},{"amount":914,"id":16520,"full_name":"Бальоха Даниїл Артемович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XU4RFtkf%2FH0a67sJVGP3rvaj2rg6e4T9CPXdOkpMba28%3D","position":7},{"amount":891,"id":16577,"full_name":"Дука Нікіта Сергійович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0X%2FL%2BKWzhSBpbjhD6pMiluscTyab2soWbZtge7WpFiths%3D","position":8},{"amount":766,"id":16519,"full_name":"Савченко Тимур Олексійович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0XGcPstkVj8lnD6XnSTuybrUnAwoIlFaxcWD5QD1ntByQ%3D","position":9},{"amount":601,"id":16388,"full_name":"Глушков Олександр Олександрович","photo_path":"https://mystatfiles.itstep.org/index.php?view_key=rtILv2awXkYrSQ7WVzOr0G9F1kZwIdRQC03dLrvYiKc%2B4a9mMOEsIcHQhr3AzM0X0THbXC4o5B6euEFGcotIUNkZzRmaFMnb90K%2Bp3%2Ba4M8%3D","position":10}]'
    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the text property
    def mock_get(*args, **kwargs):
        return MockResponse(testData)

    # apply the monkeypatch for requests.post to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # API.getkey that using patched requests.post
    result = API.GetClassLeaderboard('This is also not token')
    assert result == json.loads(testData)