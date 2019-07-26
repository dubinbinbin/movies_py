# -*- coding: utf-8 -*-
# @Author: dcb
# @Date:   2019-07-19 10:31:19
# @Last Modified by:   dcb
# @Last Modified time: 2019-07-26 10:36:34

import requests
from bs4 import BeautifulSoup
import re
import csv

requests.packages.urllib3.disable_warnings()

def pa_movies(url):
	movie_data =[]
	r = requests.get(url,verify=False)
	data = r.content.decode("gbk","ignore")
	soup = BeautifulSoup(data,"html.parser")
	l = soup.find_all("table")
	for i in l:
		# i = i.encode("utf-8")
		# print i
		try:
			# print i.find_all(text=["4.8"]			
			m = re.search("豆瓣评分(.*?)/10", str(i))
			s = m.group(1).strip()
			# f.write(s+'\n')
			# print len(s)
			m_name = i.find_all("a",attrs={'class': 'ulink'})[0]['title'].encode("utf-8")
			m_link = 'http://www.xiaopian.com' + i.find_all("a",attrs={'class': 'ulink'})[0]['href']
			movie_data.append((m_name,m_link,s))
		except Exception as e:
			pass
	return movie_data


f = open("C:\\Users\\admin\\Desktop\\tmp\\movies.csv","wb")
f_csv = csv.writer(f)
f_csv.writerow(["movie","link",'score'])

for i in range(1,308):
	if i == 1:
		url = 'http://www.xiaopian.com/html/gndy/dyzz/index.html'
		print url
		data = pa_movies(url)
		for t in data:
			f_csv.writerow(t)
	else:
		url = 'http://www.xiaopian.com/html/gndy/dyzz/index_' + str(i) + '.html'
		print url
		data = pa_movies(url)
		for t in data:
			f_csv.writerow(t)
f.close()