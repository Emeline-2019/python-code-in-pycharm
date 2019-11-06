import requests
import urllib
import chardet
if __name__ == "__main__":
    url = "https://zhidao.baidu.com/question/809602735743045532.html"
    rsp = urllib.request.urlopen(url)
    html = rsp.read()
    #print(type(rsp))
    #print(rsp)
    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    # 利用get取值保证不会出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)