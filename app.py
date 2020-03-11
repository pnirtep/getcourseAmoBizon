from flask import Flask, request
import requests

from creds import amo_user, amo_hash
from functions import get_viewers

app = Flask(__name__)

domain = 'reformalife'
user = amo_user
user_hash = amo_hash

AUTHURL = 'https://reformalife.amocrm.ru/private/api/auth.php'
CONTACTURL = 'https://reformalife.amocrm.ru/api/v2/contacts'
LEADS = 'https://reformalife.amocrm.ru/api/v2/leads'
AUTHDATA = {'USER_HASH': user_hash, 'USER_LOGIN': user}
headers = {'Content-type': 'application/json'}

# Инициализируем сессию
session = requests.Session()
response = session.get(url=AUTHURL)
authorisation = session.post(url=AUTHURL, params=AUTHDATA)


@app.route('/create')
def lead_add():
    """
    Прием данных о заказе из Геткурса и передача его в AMOCRM
    """
    user_name = request.args.get('user_name')
    user_email = request.args.get('user_email')
    user_phone = request.args.get('user_phone')
    # user_id = request.args.get('user_id')
    nomer_zakaza = request.args.get('nomer_zakaza')
    soderzhimoe = request.args.get('soderzhimoe')
    stoimost = request.args.get('stoimost')
    oplacheno = request.args.get('oplacheno')
    ostalos_oplatit = request.args.get('ostalos_oplatit')
    traffic_source = request.args.get('traffic_source')
    user_utm_source = request.args.get('user_utm_source')

    # Формируем и создаем в амо объект сделки
    LEADSDATA = {"add": [{"name": soderzhimoe, "price": stoimost}]}
    leadssend = session.post(url=LEADS, json=LEADSDATA, headers=headers)
    res_lead = leadssend.json()

    # Получаем id созданной сделки
    lead_id = res_lead['_embedded']['items'][0]['id']
    print(res_lead)

    # Создаем объект КОНТАКТ и привязываем его к нашей сделке по ее ID
    CONTACTDATA = {"add": [{"name": user_name, "leads_id": lead_id, "custom_fields": [{
        "id": "83610",
        "values": [{
            "value": user_phone,
            "enum": "WORK"
        }]
    },
        {
            "id": "83612",
            "values": [{
                "value": user_email,
                "enum": "WORK"
            }]
        }
    ]}]}
    contactsend = session.post(url=CONTACTURL, json=CONTACTDATA, headers=headers)
    res_cont = contactsend.json()
    print(res_cont)
    return 'done'


@app.route('/bizon_hook', methods=['GET', 'POST'])
def hook_data():
    """
        Принимаем исходящий из Бизона Хук после окнчания вебинара: ловим параметр webinarId для
        дальнейщего поиска массива данных о зрителях по конкретному событию
    """
    if request.method == 'POST':
        data = request.json
        web_id = data['webinarId']
        res = get_viewers(web_id)
        print(res.text)
        return "200 OK"


if __name__ == '__main__':
    app.run()
