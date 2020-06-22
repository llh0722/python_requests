# coding: utf-8
# Team : Quality Management Center
# Author：llh
# Date ：2020/6/22 14:47
# Tool ：PyCharm

import requests
# 打开登录地址
url = 'https://account.cnblogs.com/signin'
headers = {
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

s = requests.session()
r = s.get(url, headers=headers, verify=False)
print(s.cookies)

# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', '3DD49B36F41FA2C5E35705927F380722F6AB820008F90C1B81C466247B1426CE1366F559EB49A5536B1AD355BDDDE5C221F85EE78E29C256889AEF02EAF4AFF679F491FEFBC0221EA53B5E18FC42EB8274C5451F')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8B9DwO68dQFBg9xIizKsC6RUpT4RftivrKkWexp9kkA1bsdyeEAeyc8piJ75ldyk5DkLZSl4v1_Ic9quyjRTxrR1iCm957WnB7ivZFTK8gkwjvv-zzSUdIbZN_yDzwp-S1Kr3ZMZy4kAQMNAL9a4fWIYFssk1aI6m8hSaEmQk0yq91nNubtqi55nNgQdwIAsHRdOGq5xRO_r0PntewQTNAO9qf8Hq61PmyWxLNPGpsdCqE4N23uVgLwrd3zIlsJZns_GTP0N8KewCoL2TxiibUCsd5o6GSQrxG9n8u4eSvHQFAEqDQVnVGJR_VOkttkExRJOUF4Hu4nLoL2Uo6Uhe3WNrqGwx1ZDIYkA5rC97G0GKxZHk8ElYm4SlEOFg-8Q8797muxGJLHsiizbGpHPg2jXAUGsRgRUXqPVPpsqFPDhLcjdmjsN_VkqhevMJvFvFfOlalMhzrw8jwZyX8nWXj8mIkIX0SH6_OKCFiaMFkjlH7I2wkjHuymBMMbUEa9dLeWn-xxZbA3foX_My1wDOB2xVjx29z8QH-IXHC879hekl1I93-04MgnqL0c99A9NQw')  # 填上面抓包内容
c.set('AlwaysCreateItemsAsActive', "True")
c.set('AdminCookieAlwaysExpandAdvanced', "True")
s.cookies.update(c)
print(s.cookies)

# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)

# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": "村上春树",
        "Editor$Edit$EditorBody": "<p>cescesdfsd</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$Advanced$txbEntryName": "",
        "Editor$Edit$Advanced$txbExcerpt": "",
        "Editor$Edit$Advanced$tbEnryPassword": "",
        "Editor$Edit$lkbDraft": "存为草稿",
}
r2 = s.post(url2, data=body, verify=False)
print(r.content)




