# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/5 23:52'

"""
找出各个数相加等于8的组合.(这里的各个数大于0且为正数)
第一个数字拿到自己后.后面的数会先尝试所有的数.
"""

data = []


def search(rest_num):
    if rest_num <= 0:
        print(data)
    else:
        for i in range(1, rest_num + 1):
            data.append(i)  # 设置现场
            search(rest_num - i)  # 递归
            data.pop()  # 恢复现场


search(8)
