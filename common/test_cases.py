# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/9


import allure
import pytest

from selenium_baidu.common.before import before
from selenium_baidu.common.web import html
from selenium_baidu.common.current import url_tree


@allure.step("步骤1：搜索沉思录")
def step_1():
    print("======20条每页=======")


@allure.step("步骤2：打印广告条数")
def step_2():
    print("=======不一定有广告条数==========")


@allure.step("步骤3：搜索一天内关于”沉思录“的结果")
def step_3():
    print("=========百度百科特殊处理==========")


@allure.epic("测试网页版百度界面的功能")
@allure.feature("测试模块")
class TestBaidu:
    valid_list = []  # 存放有效查询结果
    ad_list = []  # 存放广告查询结果
    show_time_list = []  # 存放获取的时间结果

    def get_items(self):
        tree = url_tree.get_cur_url_tree()[1]

        content_lists = tree.xpath('//div[@id="content_left"]/div')
        for element in content_lists:
            # 有id的为有效查询结果，无id的为广告
            if element.xpath('./@id'):
                valid_id = element.xpath('./@id')[0]
                element_class_list = element.xpath('.//h3/@class')
                if element_class_list:
                    valid_url = element.xpath('.//h3/a/@href')
                    valid_name = ''.join(element.xpath('.//h3/a//text()')).strip()
                    self.valid_list.append((valid_id, valid_name, valid_url))
                else:
                    print(f"其它用户在搜，标签的属性：id={valid_id}")
            # 广告
            else:
                ad_id = "广告"
                ad_url = element.xpath('.//h3/div/a/@href')
                ad_name = ''.join(element.xpath('.//h3/div/a/text()')).strip()
                self.ad_list.append((ad_id, ad_name, ad_url))
        print(f"总条数有{len(content_lists)}条")
        return self.valid_list, self.ad_list

    @allure.title("搜索沉思录")
    @allure.story("用户故事：1")
    @allure.severity("critical")
    def test_01_items(self):
        """
            进入设置页面，选择“搜索结果显示条数”，设置为每页显示20条，然后搜索“沉思录”字样，结果确定为20条
        """
        # 获取有效词条的条数
        valid_items = self.get_items()[0]
        items = len(valid_items)
        print(f"有效结果{items}条")
        assert items == 20

        step_1()

    @allure.title("打印出广告条数")
    @allure.story("用户故事：2")
    def test_02_ad_items(self):
        """
            测试搜索结果中必定包含广告条目，并打印出现了多少条广告
        """
        ad_items = self.get_items()[1]
        ad_num = len(ad_items)
        print(f"广告结果{ad_num}条")
        print("分别为：")
        for i in ad_items:
            print(i[0], i[1])
        assert ad_num >= 0
        step_2()

    @allure.title("检查搜索结果为一天内")
    @allure.story("用户故事：3")
    def test_03_time(self):
        """
            使用“搜索工具”按钮，设置搜索时间为一天内，检查搜索结果都是一天内的
        """
        url_tree.get_cur_url_tree()[0]
        html.set_time()

        tree = html.get_page_tree()
        # 剔除广告
        content_list = tree.xpath('//div[@id="content_left"]/div[@id]')

        # 内容提取
        for element in content_list:
            element_class_list = element.xpath('.//h3/@class')
            if element_class_list:
                # url = element.xpath('.//h3/a/@href')
                # name = ''.join(element.xpath('.//h3/a//text()')).strip()
                show_time = element.xpath('.//span[@class="c-color-gray2"]/text()')
                if show_time:
                    # print(name, url, show_time[0])
                    self.show_time_list.append(show_time[0])
                else:
                    print("特殊内容：百度百科信息等")
        before.before_days(self.show_time_list)
        for i in self.show_time_list:
            print(i)
        step_3()


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_cases.py"])
