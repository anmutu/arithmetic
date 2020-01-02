# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/2 17:08'

import random


# 用递归实现二分查找的方法
def binary_recursion(left, right, data_list, target):
    if left > right:
        return -1
    mid = int((left + right) / 2)
    if target == data_list[mid]:
        return mid
    elif target > data_list[mid]:
        # 目标值大于中间值，说明目标值在右侧
        return binary_recursion(mid + 1, right, data_list, target)
    else:
        # 到这里说明目标值小于中间值，此时说明目标值在左侧
        return binary_recursion(left, mid - 1, data_list, target)


# 随机生成data的方法:从start到end生成len个随机数
def random_list(start, end, len):
    data_list = []
    for i in range(len):
        data_list.append(random.randint(start, end))
    return data_list


if __name__ == "__main__":
    data = random_list(1, 100, 10)
    data=sorted(data)
    index = random.randint(0, len(data)-1)
    pos = binary_recursion(0, len(data) - 1, data, data[index])
    print("目标值是{0}\n".format(data[index]))
    print("生成的值是{0}\n".format(data))
    if pos > 0:
        print("目标值位于{0}".format(pos))
    else:
        print("没有找到目标值")
