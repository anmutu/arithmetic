# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/7 1:11'

"""
这里是求金字塔的路线的最大值.因为也有一些值会重复用到,所以这里用了dict去做了存储.不过目前数量级较小,并没有像fib那样有具体的感知和时间的对比.
"""

from datetime import datetime

pyramid = [
    [1],
    [2, 3],
    [4, 5, 6],
]

memory = {}


def search_max(deep, y):
    if deep == 2:
        return pyramid[deep][y]
    if "{}_{}".format(deep, y) in memory:
        return memory["{}_{}".format(deep, y)]
    else:
        max_value = pyramid[deep][y] + max(search_max(deep + 1, y), search_max(deep + 1, y + 1))
        memory["{}_{}".format(deep, y)] = max_value
        return max_value


if __name__ == "__main__":
    start_time = datetime.now()
    print("这个金字塔的最大路线的值是{0}.".format(search_max(0, 0)))
    print("因数量级太小并看不到时间的优化效果,此次用时{0}s".format((datetime.now() - start_time).total_seconds()))
