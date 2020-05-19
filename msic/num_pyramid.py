# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/6 3:31'

"""
找出路径最大的值.第一步,先找出所有的路径.第二步,然后算出哪条路径是最短的.
"""

pyramid = [
    [1],
   [2, 3],
    [4, 5, 6],
    # [7, 8, 9, 10],
    # [11, 12, 13, 15]
]

data = [1]
total_path = []


def seach(deep, x, y):
    if deep == 3:
        total_path.append(data[:])
    else:
        # 第一步,选择正下方的值,将其加入到data里,且递归,且回复现场.
        data.append(pyramid[deep][y])
        seach(deep + 1, x + 1, y)
        data.pop()
        # 第二步,选择右下方的值,将其加入到data里,且递归,且回复现场.
        data.append(pyramid[deep][y+1])
        seach(deep + 1, x + 1, y + 1)
        data.pop()


if __name__ == "__main__":
    seach(1, 0, 0)
    max_value = 0
    max_index = 0
    for index, data in enumerate(total_path):
        if sum(data) > max_value:
            max_value = sum(data)
            max_index = index
    print("总共有路线如下:{0},其中{1}这个路线的值最大.".format(total_path, total_path[max_index]))

