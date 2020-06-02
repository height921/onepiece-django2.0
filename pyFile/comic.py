#!python
# -*- encoding:utf-8 -*-
# Created by admin at 2020/5/13

"""
爬虫：爬取风之动漫海贼王的图片
"""
import time
from selenium import webdriver
import os
import requests
import re
from bs4 import BeautifulSoup

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()
base_url = 'https://manhua.fzdm.com/02//'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

"""
def get_image_address(url):
    browser.get(url)
    # time.sleep(0.5)
    browser.implicitly_wait(20)
    img = browser.find_element_by_xpath("//*[@id='mhpic']")
    is_end = False
    # navigation = browser.find_element_by_xpath('//*[@id="pjax-container"]/div[2]')
    # if len(navigation.find_element_by_class_name("pure-button pure-button-primary"))==1:
    #     is_end=True
    return is_end, img.get_attribute('src')

"""


def get_image_url(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.apparent_encoding
    except requests.exceptions.HTTPError as e:
        return 0
    text = response.text
    # image_url = re.findall('var mhurl="(.*?)', text)
    image_url = re.findall('var mhurl="(.*?)"', text)

    return 'http://www-mipengine-org.mipcdn.com/i/p3.manhuapan.com/'+image_url[0]


def download_chapter(number):
    path = "E:\\python\\django\\demo1\\media\\images"
    path = os.path.join(path, str(number))
    print("准备下载"+path)
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(300):
        url = base_url+str(number)+'/index_'+str(i)+'.html'
        print(url)
        image_src = get_image_url(url)
        if(image_src == 0):
            break
        print(image_src)
        with open(path+'\\'+str(i)+'.png', 'wb') as f:
            f.write(requests.get(image_src).content)
    print("下载完成")


# download_chapter(980)
for i in range(971, 977):
    download_chapter(i)

