#coding = utf-8
import re,sys
import requests
import os
from bs4 import BeautifulSoup
import urllib
i = range(11)
shuzi = 1
for a in i:
	url = "http://www.freebuf.com/user/myfavorites/page/%s" %a
	headers = {"cookie":"zhelishicookie"}
	get1 = requests.get(url,headers=headers)
	regex = "\<a href=\'(.*?)\' title=\'(.*?)\'\>(.*?)\<\/a\>\<\/div\>"
	key = re.findall(regex,get1.content)
	try:
		for k in key:
			print get1.url
			print k[0]
			get2 = requests.get(k[0])
			print get2.url
			if os.path.exists(k[1].decode('utf-8') + '.html') ==False:
				print 'meiyou'*50
				bc = open(k[1].decode('utf-8') + '.html','w+')
				bc.write(get2.content)
				neirong2 = get2.content
				soup = BeautifulSoup(neirong2,from_encoding='gbk')
				img = soup.findAll('img')
				print img
				for m in img:
					g = m.get('src')
					print g
					try:
						
						imgg = g.split('/')[-1]
						print imgg	
						print 'a'*20
						urllib.urlretrieve(g,imgg)
					except:
						
						break

	except:
		for k in key:
			print get1.url
			print k[0]
			get2 = requests.get(k[0])
			print get2.url
			if os.path.exists(str(shuzi) + '.html') ==False:
				print 'meiyou'*50
				bc = open(str(shuzi) + '.html','w+')
				bc.write(get2.content)
				shuzi+=1
				print shuzi
				neirong2 = get2.content
				soup = BeautifulSoup(neirong2,from_encoding='gbk')
				img = soup.findAll('img')
				print img
				for m in img:
					g = m.get('src')
					print g
					try:
						
						imgg = g.split('/')[-1]
						print imgg	
						print 'a'*20
						urllib.urlretrieve(g,imgg)
					except:
					
						break



//爬取的是http://www.freebuf.com/user/myfavorites这里freebuf个人中心收藏的文章，如果你收藏的比较多，按需修改第七行代码处的“i = range(11)”。由于windows下文件名不能出现特殊符号，所以如果有特殊符号，则保存的文件名为数字.html。
如果不小心把爬取下载的窗口关了也没事，可重新运行，会判断文件是否存在，只会下载没下载过的。
图片没有分类，全部下载同一个目录里的，全部下载完了，记得把<img src>中的图片路径改成相对路径。
