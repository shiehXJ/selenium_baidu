# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/9
# 将在百度网页搜索界面的基本操作封装起来

import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions


option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
brw = webdriver.Chrome(options=option)
brw.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                    {'source': 'Object.defineProperty(navigator,"webdriver",'
                               '{get:()=>undefind})'})


class Baidu:
    # 建立连接
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self):
        pass

    # 关闭驱动
    def teardown(self):
        self.driver.quit()

    # 打开百度
    def open_baidu(self, base_url):
        self.driver.get(base_url)
        self.driver.maximize_window()

    # 打开搜索设置
    def set_setting(self):
        self.driver.find_element(By.ID, "s-usersetting-top").click()
        self.driver.find_element(By.XPATH, '//a[@class="setpref first"]/span[@class="set"]').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "nr_2")))
        self.driver.find_element(By.ID, "nr_2").click()
        # num = self.driver.find_element(By.ID, "nr_2").get_attribute("value")

        self.driver.find_element(By.LINK_TEXT, "保存设置").click()

    # 输入关键字，点击百度一下
    def click_baidu(self, key_word):
        self.driver.find_element(By.ID, "kw").click()
        # 输入关键字：“沉思录”
        self.driver.find_element(By.ID, "kw").send_keys(key_word)
        # 点击“百度一下”
        self.driver.find_element(By.ID, "su").click()

    # 获取当前页面的url
    def get_current_url(self):
        return self.driver.current_url

    # 获取网页源码
    def get_page_tree(self):
        source = self.driver.page_source
        tree = etree.HTML(source)
        return tree

    # 等待,type_id =1 显示等待  type_id = 2 隐式等待 type_id = 3 强制等待
    def page_wait1(self, locate):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locate))

    def page_wait2(self):
        self.driver.implicitly_wait(30)

    # 关闭alert弹窗
    def close_alert(self):
        self.driver.switch_to.alert.accept()

    # 设置时间选择器
    def set_time(self):
        # 设置搜索工具-选择一天内
        self.driver.find_element(By.XPATH, '//div[@id="tsn_inner"]/div[2]/div').click()
        # 时间选择器
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "timeRlt")))

        self.driver.find_element(By.XPATH, '//div[@class="options_2Vntk"]//span[@id="timeRlt"]').click()

        # 选择一天内
        print(self.driver.find_element_by_xpath('//ul[@class="file_ul_2a1K5"]/li[2]').text)
        self.driver.find_element(By.XPATH, '//ul[@class="file_ul_2a1K5"]/li[2]').click()
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, "content_left")))
        time.sleep(5)


html = Baidu()
