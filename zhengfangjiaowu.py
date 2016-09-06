# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url = 'http://222.24.62.120/'
authcode_url = 'http://222.24.62.120/CheckCode.aspx'
post_url = 'http://222.24.62.120/default2.aspx'
s = requests.Session()
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '193',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': '222.24.62.120',
    'Origin': 'http://222.24.62.120',
    'Referer': 'http://222.24.62.120/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36'
}

header1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '222.24.62.120',
    'Referer': 'http://222.24.62.120/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36',
}


r = s.get(url, headers=header1)
r.encoding = 'gbk'
doc = r.text


soup = BeautifulSoup(doc, 'html.parser')
VIEWSTATE = soup.find('input', type="hidden")
value = VIEWSTATE['value']


image = s.get(authcode_url, headers=header1)
with open('/home/huerke/Desktop/rrrr.jpg', 'wb') as fd:
    for chunk in image.iter_content():
        fd.write(chunk)

txtSecretCode = raw_input('pls enter authcode')


postdata = {
    'txtUserName': '你的学号',
    'TextBox2': '你的密码',
    'RadioButtonList1': '学生',
    'Button1': '',
    'lbLanguage': '',
    'hidPdrs': '',
    'hidsc': '',
}
postdata['__VIEWSTATE'] = value
postdata['txtSecretCode'] = txtSecretCode

login_page = s.post(post_url, data=postdata, headers=header)
r = s.get('http://222.24.62.120/xs_main.aspx?xh=03133045')
r.encoding = 'gbk'
doc = r.text
print doc
