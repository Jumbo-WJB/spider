#coding = utf-8
import requests,re
import urllib
import sys
yeshu = range(1,6)
xiangmuming = raw_input('github:')
for page in yeshu:
    url = 'https://github.com/%s?page=%s&tab=repositories' %(xiangmuming,page)
    get = requests.get(url)
    # print get.url
    #print get.content
    regex = '\<a href=\"(.*?)\" itemprop\=\"name codeRepository\"\>'
    key = re.findall(regex,get.content)
    # print key
    for k in key:
        # print k
        xiangmudizhi = 'https://github.com/' + k
        # print xiangmudizhi
        qingqiu = requests.get(xiangmudizhi)
        print qingqiu.url
        xiazai = '/archive/master.zip'
        down = qingqiu.url + xiazai
        print down
        kaishixiazai = urllib.urlopen(down)
        aaaa = kaishixiazai.info()
        #print aaaa
        filenameRe = re.compile(r'Content-Disposition: attachment; filename=(.*)')
        filename = re.findall(filenameRe, str(aaaa))
        #print filename
        for file in filename:
            #print file
            name = file.strip()
            print name
            urllib.urlretrieve(down, name)
