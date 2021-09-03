# -*- coding:utf-8 -*-

"""
时间:2021年09月03日
作者:幻非
"""

from selenium import webdriver

print("打开网页后进行登陆操作，登陆完毕后输入任意字符程序将自动关闭并生成cookie文件")

url = "https://www.epicgames.com/store/zh-CN/free-games"

driver = webdriver.Chrome()
driver.get(url)
# 登录后输入任意字符
input()
# 获取cookie
cookie = driver.get_cookies()
# 写入cookie
with open('cookie.txt', 'w') as f:
    f.write(str(cookie))

print(cookie)
driver.quit()


"""
参考资料:
https://www.cnpython.com/qa/26852
https://www.bilibili.com/video/BV1po4y1S7zT
"""
