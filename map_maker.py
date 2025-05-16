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
map_file = "easy_киев.png"
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


ll_spn = '39.893813,57.626559&spn=3,3'
pt = "39.893813,57.626559,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy6.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '2.1734035,41.3850639&spn=5.5,5.5'
pt = "2.1734035,41.3850639,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy7.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '28.9497,41.0138&spn=6,6'
pt = "28.9497,41.0138,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy8.png"
with open(map_file, "wb") as file:
    file.write(response.content)



ll_spn = '18.0649,59.3326&spn=6,6'
pt = "18.0649,59.3326,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy9.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '139.692,35.6895&spn=6,6'
pt = "139.692,35.6895,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy10.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '116.397,39.9075&spn=7,7'
pt = "116.397,39.9075,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_пекин.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-99.1277,19.4285&spn=7,7'
pt = "-99.1277,19.4285,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_мехико.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '16.3721,48.2085&spn=7,7'
pt = "16.3721,48.2085,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_вена.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '135.084,48.4827&spn=7,7'
pt = "135.084,48.4827,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_хабаровск.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-58.3772,-34.6132&spn=10,10'
pt = "-58.3772,-34.6132,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_буэнос-айрес.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '71.446,51.1801&spn=7,7'
pt = "71.446,51.1801,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_астана.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-75.6981,45.4112&spn=7,7'
pt = "-75.6981,45.4112,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_оттава.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '14.4208,50.088&spn=7,7'
pt = "14.4208,50.088,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_прага.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '24.9354,60.1695&spn=7,7'
pt = "24.9354,60.1695,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_хельсинки.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '27.5667,53.9&spn=7,7'
pt = "27.5667,53.9,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_минск.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '149.128,-35.2835&spn=7,7'
pt = "149.128,-35.2835,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_канберра.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '45.1749,54.1838&spn=7,7'
pt = "45.1749,54.1838,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_саранск.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '9.18951,45.4643&spn=7,7'
pt = "9.18951,45.4643,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_милан.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '105.841,21.0245&spn=7,7'
pt = "105.841,21.0245,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_ханой.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '13.1873,32.8874&spn=7,7'
pt = "13.1873,32.8874,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_триполи.png"
with open(map_file, "wb") as file:
    file.write(response.content)



ll_spn = '-122.332,47.6062&spn=7,7'
pt = "-122.332,47.6062,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_сиэтл.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '69.2163,41.2646&spn=7,7'
pt = "69.2163,41.2646,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_ташкент.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-82.383,23.133&spn=7,7'
pt = "-82.383,23.133,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_гавана.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '36.2913,33.5102&spn=7,7'
pt = "36.2913,33.5102,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_дамаск.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-70.6483,-33.4569&spn=7,7'
pt = "-70.6483,-33.4569,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_сантьяго.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-70.6483,-33.4569&spn=7,7'
pt = "-70.6483,-33.4569,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_сантьяго.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '13.4105,52.5244&spn=7,7'
pt = "13.4105,52.5244,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy_берлин.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-0.12574,51.5085&spn=7,7'
pt = "-0.12574,51.5085,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy_лондон.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '33.0925,68.9792&spn=7,7'
pt = "33.0925,68.9792,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy_мурманск.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '23.7278,37.9838&spn=7,7'
pt = "23.7278,37.9838,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy_афины.png"
with open(map_file, "wb") as file:
    file.write(response.content)

ll_spn = '31.2497,30.0626&spn=7,7'
pt = "31.2497,30.0626,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy_каир.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '55.1713,25.0657&spn=7,7'
pt = "55.1713,25.0657,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "easy_дубай.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '46.0086,51.5406&spn=7,7'
pt = "46.0086,51.5406,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_саратов.png"
with open(map_file, "wb") as file:
    file.write(response.content)

ll_spn = '-80.1937,25.7743&spn=7,7'
pt = "-80.1937,25.7743,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_майами.png"
with open(map_file, "wb") as file:
    file.write(response.content)

ll_spn = '151.207,-33.8679&spn=7,7'
pt = "151.207,-33.8679,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_сидней.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '18.4232,-33.9258&spn=7,7'
pt = "18.4232,-33.9258,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_кейптаун.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '60.6122,56.8519&spn=7,7'
pt = "60.6122,56.8519,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_екатеринбург.png"
with open(map_file, "wb") as file:
    file.write(response.content)

ll_spn = '114.175,22.2783&spn=7,7'
pt = "114.175,22.2783,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "medium_гонконг.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '14.5051,46.0511&spn=7,7'
pt = "14.5051,46.0511,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_любляна.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '9.52154,47.1415&spn=7,7'
pt = "9.52154,47.1415,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_вадуц.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '19.8189,41.3275&spn=7,7'
pt = "19.8189,41.3275,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_тирана.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '-2.97794,53.4106&spn=7,7'
pt = "-2.97794,53.4106,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_ливерпуль.png"
with open(map_file, "wb") as file:
    file.write(response.content)

ll_spn = '38.7469,9.02497&spn=7,7'
pt = "38.7469,9.02497,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_аддис-абеба.png"
with open(map_file, "wb") as file:
    file.write(response.content)


ll_spn = '40.4414,56.4281&spn=7,7'
pt = "40.4414,56.4281,pm2dbl"
map_request = f"{server_address}{ll_spn}&apikey={api_key}&pt={pt}&style=tags.all:locality|stylers.visibility:off"
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
map_file = "hard_суздаль.png"
with open(map_file, "wb") as file:
    file.write(response.content)
