import requests
import json
import time


data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/krw/eth?interval=6h')
# print(data.content)

loads = json.loads(data.content)  # 싱글 따옴표로 바뀜
print(loads)

for i in range(200):
    print("==========================")
    dt_ = loads['body']['candles'][i]['dt']
    strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dt_ / 1000))  # 시간 형식으로 바꾸기 13자리기 때문에 1000을 나눠야됨
    print(strftime)
    print(loads['body']['candles'][i]['close'])  # a.json 참고
