# -*- coding: utf-8 -*-
# @author: xiejuan
# @email: xiejuanchn@163.com
# @date: 2022/7/9
# 判断搜索词条的时间是否为一天内

class Before:
    def before_days(self, show_list):
        """
        返回list元素中的数字，并判断该数字是否小于24h
        1. list是小时，则数字小于24
        2. list是分钟，则数字小于60
        3. list是秒，则数字小于60
        :param show_list: >list
        """
        date_time = ["小时", "分钟", "秒"]
        print()
        for tim in show_list:
            tim = tim + ""
            tim = tim.strip()
            tim1 = tim.strip().split(date_time[0])[0]
            if not tim1.isdigit():
                tim2 = tim1.strip().split(date_time[1])[0]
                if not tim2.isdigit():
                    tim3 = tim2.strip().split(date_time[2])[0]
                    if tim3.isdigit():
                        assert int(tim3) <= 60
                else:
                    assert int(tim2) <= 60
            else:
                assert int(tim1) <= 24


before = Before()
