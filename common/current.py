# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/9
# 返回当前页面的url和源码

from selenium.webdriver.common.by import By
from selenium_baidu.common.web import html


class UrlTree:
    base_url = "https://www.baidu.com"
    # 设置为20条后的的url

    def get_cur_url_tree(self):
        """
        返回当前页面的url和当前页面的源码
        :return:
        cur_url：当前页面的url
        cur_html：当前页面的源码
        """
        html.setup()
        html.open_baidu(self.base_url)
        html.set_setting()
        html.page_wait2()
        html.page_wait2()

        html.close_alert()

        html.click_baidu("沉思录")
        html.page_wait1((By.ID, "content_left"))

        cur_url = html.get_current_url()
        cur_html = html.get_page_tree()
        return cur_url, cur_html


url_tree = UrlTree()
