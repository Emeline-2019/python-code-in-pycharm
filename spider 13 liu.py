# cookiejar 的案例
# coding=utf-8                           #   这个不放就会报错，为什么？？？

# 创建cookiejar的实例

from http import cookiejar
from urllib import request, parse

cookie = cookiejar.CookieJar()
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)
def login():
    """
    负责初次登陆
    需要输入用户名密码，用来获取登陆cookie凭证

    """
    #此url需要从登陆form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    # 此键值需要从登陆的两个对应input中提取name属性
    data = {"email":"18069758701","password":"123456love"}
    # 把数据进行编码
    data = parse.urlencode(data)
    #创建一个请求对象
    req = request.Request(url,data=data.encode("utf-8"))        # 为什么不能进入到我的主页，还是在登陆界面？？？
    #使用opener发起请求
    rsp = opener.open(req)
def getHomePage():
    url = "http://www.renren.com/972277637/newsfeed/origin"
    #如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open ("rsp.html","w") as f:
         f.write(html)
if __name__ == "__main__":
    login()
    getHomePage()