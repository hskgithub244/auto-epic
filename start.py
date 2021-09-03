# -*- coding:utf-8 -*-

"""
时间:2021年09月03日
作者:幻非
"""

from selenium import webdriver

with open("cookie.txt", "rb") as file:
    cookies = eval(file.readline())
    print(cookies)

url = "https://www.epicgames.com/store/zh-CN/free-games"

driver = webdriver.Chrome()
driver.get(url)
# 删除所有cookie
driver.delete_all_cookies()
# 加入cookie
for cookie in cookies:
    driver.add_cookie(cookie)
# 刷新网页
driver.refresh()

"""
参考资料:
https://www.cnpython.com/qa/26852
https://www.bilibili.com/video/BV1po4y1S7zT
"""
