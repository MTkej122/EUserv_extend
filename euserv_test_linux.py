import cmd
import os
import sys
import time
import re
import json
import time
import requests
from bs4 import BeautifulSoup
from requests import post

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
# 加载webdriver对象驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox') # 这个很重要
driver = webdriver.Chrome(options=chrome_options) # chromedriver环境加载
email = input('请输入你的德鸡邮箱或ID' + '\n')
password = input('请输入你的德鸡密码' + '\n')

# 打开euserv登录界面
driver.get('https://support.euserv.com/')
time.sleep(5)
"""
TG 消息推送
"""
TG_TOKEN = '1998512573:AAGV8opjbSXEBhNhKYxP11d-rfV6L1FNcJI'
CHAT_ID = '1470843414'


def post_tg(message):
    telegram_message = f"{message}"

    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Markdown"),  # 可选Html或Markdown
        ('disable_web_page_preview', "yes")
    )
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    telegram_req = post(telegram_url, params=params)
    telegram_status = telegram_req.status_code
    if telegram_status == 200:
        print(f"INFO: Telegram Message sent")
    else:
        print("Telegram Error")


def iselement():
    """
    基本实现判断元素是否存在
    :param browser: 浏览器对象
    :param xpaths: xpaths表达式
    :return: 是否存在
    """
    try:
        driver.find_element_by_xpath('//*[@id="kc2_order_customer_orders_tab_0"]')
        return True
    except:
        return False


driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('Submit').click()
d = iselement()
if d == False:
    print("登录失败,请检查用户名及密码!!")
    sys.exit(1)
time.sleep(2)
try:
    x = driver.find_element_by_xpath(
        '//*[@id="kc2_order_customer_orders_tab_content_0"]/div/div[1]/table/tbody/tr[2]/td[1]/img')
    driver.find_element_by_link_text('extend contract').click()
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="kc2_customer_contract_details_change_plan_item_container_13448"]/tbody/tr/td[2]/input').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="kc2_security_password_dialog_form"]/input[4]').send_keys('kujie2001')
    driver.find_element_by_id('kc2_security_password_dialog_action_confirm').click()
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="kc2_customer_contract_details_extend_contract_confirmation_dialog_action_container"]/input[2]').click()
    post_tg("运行完毕！德鸡 " + email + "已到续期时间点，成功续期!")
    print('德鸡续费成功!')
except:
    post_tg("运行完毕！德鸡" + email + "未到续期时间点，后会有期！")
    print("无续费小鸡")
