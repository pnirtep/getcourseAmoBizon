import json
import requests
import base64
from creds import getcourse_token

lead_url = 'https://reformalife.getcourse.ru/pl/api/deals'
user_url = 'https://reformalife.getcourse.ru/pl/api/users'
token = getcourse_token


def create_user():
    user_data = {
        "user":
            {"email": "pnirtep@test.com",
             "phone": "89190381819",
             "first_name": "User",
             "last_name": "Test",
             "city": "Москва",
             "country": "Россия"},
        "system": {"refresh_if_exists": 0}
    }

    json_user = json.dumps(user_data, ensure_ascii=False)
    d = base64.b64encode(json_user.encode())
    data = {"action": "add", "key": token, "params": d}
    req = requests.post(url=user_url, data=data)
    return print(req.text)


create_user()
