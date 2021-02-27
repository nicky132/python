import urllib.request
res = urllib.request.urlopen("http://www.baidu.com")
print (res.read().decode('utf-8'))