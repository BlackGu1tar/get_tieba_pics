# -*- coding=utf-8 -*-


import urllib,re,requests
from bs4 import BeautifulSoup


def get_page(url):
	html_page = requests.get(url).content
	soup = BeautifulSoup(html_page,'html.parser')
	imgs = soup.find_all('img',class_='BDE_Image')
	return imgs

#获取只看楼主后总页数
def get_number(url):
	html_page = requests.get(url).content
	soup = BeautifulSoup(html_page,'html.parser')
	page_number = soup.find_all('span',class_='red')
	page_no = page_number[1].string
	return page_no

input_id = raw_input('Enter tieba_url ID : ')
url_head = 'https://tieba.baidu.com/p/'
url_str = '?see_lz=1'
url_addr = url_head+input_id+url_str
pages_number = int(get_number(url_addr))


tmp = 0
for x in range(1,pages_number):
	imgurl = url_addr+str(x)
	for y in get_page(imgurl):
		src_url = y.get('src')
		try:
			urllib.urlretrieve(src_url,'C:\\pics\\%s.jpg' %tmp)
			tmp+=1
			print src_url+'		***Downling Success!***'
		except Exception as e:
			raise e