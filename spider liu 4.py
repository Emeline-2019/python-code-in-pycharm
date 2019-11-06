import chardet
from urllib import request
if __name__ == "__main__":
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)
    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))


    print("&"*50)

    html = rsp.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    # html = html.decode(cs.get("encoding", "utf-8"))   # 这个解码方式和下面这个解码方式有啥区别
    html = html.decode("gbk")   # 为什么不能用utf-8？？？？
    print(html)