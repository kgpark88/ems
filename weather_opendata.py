# https://www.data.go.kr/data/15057682/openapi.do
# 상세기능 : 동네예보조회

import requests
from datetime import date, datetime

sky_code = ['맑음', '구름조금', '구름많음', '흐림']
today = date.today()
today_str = today.strftime('%Y%m%d') 

ServiceKey ='발급받은 API키 입력'
pageNo =1
numOfRows = 10
dataType ='JSON'
# 발표일 : 20200609, 발표시간(1일 8회) : 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300 
base_date = today_str  
base_time ='0800' 
# 방이1동 X, Y 좌표 : 기상청18_동네예보+조회서비스_오픈API활용가이드_격자_위경도.xlsx 참조
nx = '62' 
ny = '125'

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService'
url += '/getVilageFcst?ServiceKey={}&pageNo={}&numOfRows={}&dataType={}&base_date={}&base_time={}&nx={}&ny={}'.format(ServiceKey, pageNo, numOfRows, dataType, base_date,base_time, nx, ny)
print(url)
print('')


resp = requests.get(url)

if resp.status_code == 200:
    resp_json = resp.json()
    response = resp_json['response']
    result_msg = response['header']['resultMsg']

    if result_msg == 'NORMAL_SERVICE':
        body_data = response['body']
        for w in body_data['items']['item']:
            category = w['category']
            if category == 'SKY':
                sky = int(w['fcstValue'])
            elif category == 'T3H':
                temperature = float(w['fcstValue'])
            elif category == 'REH':
                humidity = float(w['fcstValue'])                
        print("하늘 : {}, 온도 : {}, 습도 : {}".format(sky_code[sky-1], temperature, humidity))
    else:
        print(result_msg)




