#создание карт

import sys
import requests

server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

ll_spn = 'll=30.5238,50.4547&spn=7,7'
pt = "30.5238,50.4547,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy1.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = 'll=37.6156,55.7522&spn=6,6'
pt = "37.6156,55.7522,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy2.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = 'll=2.3488,48.8534&spn=5,5'
pt = "2.3488,48.8534,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy3.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-74.006,40.7143&spn=7,7'
pt = "-74.006,40.7143,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy4.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-74.006,40.7143&spn=7,7'
pt = "-74.006,40.7143,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy4.png"
with open(map_file, "wb") as file:
    file.write(response.content)

ll_spn = '12.496176,41.902695&spn=7,7'
pt = "12.496176,41.902695,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy5.png"
with open(map_file, "wb") as file:
    file.write(response.content)
