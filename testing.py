from datetime import datetime
import time
import iso8601

x = {"errors": [], "viewers":
    [{"playVideo": 1, "email": "pnirtep@yandex.ru", "phone": "+79190381801", "username": "Иван Иванов",
      "url": "https://vebinar.azpro.ru/room/test", "ip": "95.107.119.211",
      "useragent": "Microsoft Windows, Chrome 80.0.3987.132", "referer": "https://vebinar.azpro.ru/room/test",
      "cu1": "", "p1": "", "p2": "", "p3": "", "roomid": "11991:test", "chatUserId": "rfMzt0fHL", "city": "Калуга",
      "country": "RU", "region": "Калужская область", "tz": "", "created": "2020-03-08T20:43:59.042Z",
      "webinarId": "11991:test*2020-03-08T23:43:47", "view": 1583700236751, "viewTill": 1583700251042,
      "messages_num": 0, "finished": True},
     {"playVideo": 0, "email": "pnirtep@gmail.com", "phone": "+79199999999", "username": "Джек Блэк",
      "url": "https://vebinar.azpro.ru/room/test", "ip": "95.107.119.211",
      "useragent": "Microsoft Windows, Edge 18.18362", "referer": "https://vebinar.azpro.ru/room/test", "cu1": "",
      "p1": "", "p2": "", "p3": "", "roomid": "11991:test", "chatUserId": "BGUGY0GHL", "city": "Калуга",
      "country": "RU", "region": "Калужская область", "tz": "", "created": "2020-03-08T20:43:59.111Z",
      "webinarId": "11991:test*2020-03-08T23:43:47", "view": 1583700241823, "viewTill": 1583700241823,
      "messages_num": 0, "finished": True}], "total": 2, "skip": 0, "limit": 1000, "loaded": 2}


class Viewer():
    def __init__(self, name, phone, email, finished, endwatch, endweb):
        self.name = name
        self.phone = phone
        self.email = email
        self.finished = finished
        self.endwatch = endwatch
        self.endweb = endweb

    def count_time(self):
        data = iso8601.parse_date(self.endweb)
        end_web = data.timestamp()
        timestamp = self.endwatch/1000
        watch_time = timestamp - end_web
        return watch_time

    def tag_status(self, watch_time):
        if watch_time >= 3600:
            self.tag = 'Горячий'
        else:
            self.tag = 'Холодный'
        return self.tag


total_viewers = x['total']

users = []
for i in range(0, total_viewers):
    user = Viewer(x['viewers'][i]['username'],
                  x['viewers'][i]['phone'],
                  x['viewers'][i]['email'],
                  x['viewers'][i]['finished'],
                  x['viewers'][i]['viewTill'],
                  x["viewers"][i]['created']
                  )
    users.append(user)

#Проверка
users[0].count_time()
users[1].count_time()

for user in users:
    print(user.tag_status(user.count_time()))

