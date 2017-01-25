from urllib.request import urlopen
from bs4 import BeautifulSoup


japi = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4111760000" 
response = urlopen(japi)
weather = BeautifulSoup(response, "html.parser")
    
    
for data in weather.findAll('data'):
    hour = data.hour.string
    temp = data.temp.string
    reh  = data.reh.string
    print ("Hour : %2s, Temperature : %04s, Humidity : %02s "  % ( hour, temp, reh ))
    



 
