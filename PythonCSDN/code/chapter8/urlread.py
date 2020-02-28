import urllib.request
#urlopen(url, data=None):打开url对应的资源
with urllib.request.urlopen('http://crazyit.org/index.php') as f:
    print(f.read().decode('UTF-8'))
