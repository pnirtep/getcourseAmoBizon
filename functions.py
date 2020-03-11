from creds import bizon_token
import requests


def get_viewers(id):
    """
        Получаем данные о конкретном вебинаре с использованием его ID.
    """
    token = bizon_token
    head = {'X-Token': token, 'Content-type': 'application/json'}
    url = 'https://online.bizon365.ru/api/v1/webinars/reports/getviewers?webinarId={}'.format(id)
    req = requests.get(url=url, headers=head)
    print(req.text)
    return req