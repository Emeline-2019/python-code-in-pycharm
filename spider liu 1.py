# 使用urllib.request请求一个网页内容，并把内容打印出来
from urllib import request
if __name__ =="__main__":
     url = "https://jobs.51job.com/shenzhen-nsq/116475870.html?s=01&t=0"
     # 打开相应URL并把相应页面作为返回
     rsp = request.urlopen(url)
     # 把返回结果读取出来
     # 读取出来的内容类型为bytes
     html = rsp.read()
     print(type(html))
     # 如果想把bytes内容转换成字符串，需要解码
     html = html.decode("gbk")    # 为什么这里不能用utf-8？？？？？？
     print(html)
