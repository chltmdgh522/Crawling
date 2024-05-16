import requests
import json
from multiprocessing.dummy import Pool as ThreadPool # dummy를 쓰면 멀티쓰레딩임 아니면 그냥 멀티프로세싱


url = [
    "https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1689595200000&interval=6H&1715506970386",
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1693915200000&interval=6H&1715506970252',
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1685275200000&interval=6H&1715506970577',
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1680955200000&interval=6H&1715506970666',
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1676635200000&interval=6H&1715506970937',
    'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1672315200000&interval=6H&1715506971389',
]
print(url[0])

def crawling(url):
    data = requests.get(url)
    loads = json.loads(data.content)  # 싱글 따옴표로 바뀜
    return loads['body']['candles'][0]['close']


# for i in url:
#     crawling1 = crawling(i)
#     print(crawling1)


pool = ThreadPool(4)
result = pool.map(crawling, url)
pool.close()
pool.join()

print(result) # 반복문 보다 더 빠름