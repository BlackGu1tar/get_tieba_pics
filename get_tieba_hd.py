# -*- coding=utf-8 -*-


import urllib,re,requests
from bs4 import BeautifulSoup

#获取图片URL
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

tieba_id = raw_input('Enter tieba ID : ')
tieba_head ='https://tieba.baidu.com/p/'
url_pic_head = 'http://imgsrc.baidu.com/forum/pic/item/'

tieba_str = '?see_lz=1&pn='
tieba_addr = tieba_head + tieba_id + tieba_str
tieba_addr1 = tieba_head + tieba_id + tieba_str
pages_number = int(get_number(tieba_addr1))+1

for x in range(1,pages_number):
	imgurl = tieba_addr+str(x)
	for s in get_page(imgurl):
		src_url = s.get('src')
		file_name = re.findall('([A-Za-z0-9][-A-Za-z0-9]+\.jpg)',src_url)
		jpgs_name = ''.join(file_name)
		pics_url = url_pic_head + jpgs_name   #获取组合http_url头部和文件名后的URL
		try:
			urllib.urlretrieve(pics_url,'C:\\pics\\%s' %jpgs_name)
			print pics_url +'	 *Downling Success!*'
		except Exception as e:
			raise e		





