import chardet
from urllib import request
if __name__ =="__main__":
     url = "https://jobs.51job.com/shenzhen-nsq/116475870.html?s=01&t=0"
     # 打开相应URL并把相应页面作为返回
     rsp = request.urlopen(url)
     # 把返回结果读取出来
     # 读取出来的内容类型为bytes
     html = rsp.read()
     cs = chardet.detect(html)
     html = html.decode(cs.get("encoding", "utf-8"))
     print(html)