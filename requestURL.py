import urllib.request

# 抓取网页：第一种方法_最简单
url = "http://www.douban.com"
print('第一种方法')
response1 = urllib.request.urlopen(url)
html1 = response1.read()
print('code1:', response1.getcode())
print('length1:', len(html1))

# 抓取网页：第二种方法_request
req = urllib.request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(req)
html2 = response2.read()
print('code2:', response2.getcode())
print('length2:', len(html2))

# 抓取网页：第三种方法_添加特殊情景的处理器
# create a password manager
pw = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# add the username and password.
