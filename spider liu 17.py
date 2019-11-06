# requests的案例
import requests
url = "https://www.baidu.com"
rsp = requests.get(url)
print(rsp.text)
