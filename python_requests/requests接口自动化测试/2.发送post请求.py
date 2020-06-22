# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/6/22 14:21
# Tool ：PyCharm

import requests

'''
一、查看官方文档
1.学习一个新的模块，其实不用去百度什么的，直接用help函数就能查看相关注释和案例内容。
>>import requests
>>help(requests)

2.查看python发送get和post请求的案例
 >>> import requests
       >>> r = requests.get('https://www.python.org')
       >>> r.status_code
       200
       >>> 'Python is a programming language' in r.content
       True
    
    ... or POST:
    
       >>> payload = dict(key1='value1', key2='value2')
       >>> r = requests.post('http://httpbin.org/post', data=payload)
       >>> print(r.text)
       {
         ...
         "form": {
           "key2": "value2",
           "key1": "value1"
         },
         ...
       }
'''

'''
二、发送post请求
1.用上面给的案例，做个简单修改，发个post请求
2.payload参数是字典类型，传到如下图的form里

payload = {
    'yoyo': 'helloword',
    'python qq群': "324234234"
}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

返回结果
{
    "args":{},
    "data": "",
    "form": {
         'yoyo': 'helloword',
         'python qq群': "324234234"
    },
    "code": ""
}
'''


'''
三、json
1.post的body是json类型，也可以用json参数传入。
2.先导入json模块，用dumps方法转化成json格式。
3.返回结果，传到data里
import json
payload = {
    'yoyo': 'helloword',
    'python qq群': "324234234"
}
data_json = json.dumps(payload)
r = requests.post('http://httpbin.org/post', data=data_json)
print(r.text)
'''

'''
四、headers
1.以禅道登录为例，模拟登陆，这里需添加请求头headers,可以用fiddler抓包
2.讲请求头写成字典格式
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": "xxx.............",    # 此处cookie省略了
            "Connection": "keep-alive"
            }
'''


'''
五、禅道登录参考代码

# 禅道host地址
host = "http://127.0.0.1"

def login(s,username,psw):
    url = host+"/zentao/user-login.html"
    # 请求头header
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": host+"/zentao/user-login.html",
        # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        }
    
    # 登录参数
    body1 = {"account": username,
             "password": psw,
             "keepLogin[]": "on",
             "referer":  host+"/zentao/my/"
            }

    # s = requests.session()   不要写死session

    r1 = s.post(url, data=body1, headers=h)
    # return r1.content  # python2的return这个
    return r1.content.decode("utf-8")  # python3

def is_login_sucess(res):
        if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
                return False
        elif "parent.location=" in res:
                return True
        else:
                return False

if __name__ == "__main__":
    s = requests.session()
    a = login(s, "admin", "e10adc3949ba59abbe56e057f20f883e")
    result = is_login_sucess(a)
    print("测试结果：%s"%result)
'''