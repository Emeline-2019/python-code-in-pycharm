# session 的案例
from urllib import request
import chardet
if __name__ == "__main__":
    url = "https://mail.qq.com/"
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)   # 利用chardet自动检测
    print(type(cs))
    print(cs)
    html = html.decode(cs.get("encoding", "utf-8"))   # 利用get取值保证不会出错
    print(html)
    with open("rsp.html","w") as f:
        f.write(html)

