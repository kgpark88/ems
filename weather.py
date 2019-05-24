from urllib.request import urlopen
from bs4 import BeautifulSoup

# 동네예보 : 서울특별시 송파구 방이1동
data_name = "서울특별시 송파구 방이1동"
data_code = "1171056100"
japi = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=" + data_code
response = urlopen(japi)
weather = BeautifulSoup(response, "html.parser")

print(data_name, " 동네 예보")
print("데이터 소스 :", japi)

for data in weather.findAll('data'):
    hour = data.hour.string
    temp = data.temp.string
    reh = data.reh.string
    print("시간 : %02s, 온도 : %04s, 습도 : %02s " % (hour, temp, reh ))
