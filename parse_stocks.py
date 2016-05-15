# http://paxnet.moneta.co.kr/stock/searchStock/searchStock.jsp?section=0
# http://paxnet.moneta.co.kr/stock/searchStock/searchStock.jsp?section=1

import bs4
from urllib import parse
import requests

url = 'http://paxnet.moneta.co.kr/stock/searchStock/searchStock.jsp?section=0'
response = requests.get(url)
response.encoding='cp949'
data = bs4.BeautifulSoup(response.text, 'html.parser')
trs = data.find_all('tr')
for tr in trs:
	tds = tr.find_all('a')
	for td in tds:
		print(td.text)
