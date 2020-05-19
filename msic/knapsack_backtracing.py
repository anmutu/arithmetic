# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/10 21:10'

"""
用回溯法实现背包问题
"""

# 第一列值是重量，第二列值是价值。
info = [
    [3, 8],
    [2, 5],
    [5, 12]
]

selects = []
max_selects = []
max_value = 0



def search(depth, rest):
    if depth == 3:
        print(selects)
        values = []
        for index, select in enumerate(selects):
            values.append(select * info[index][1])
        global max_value
        if sum(values) > max_value:
            max_value = sum(values)
            # print(max_value)
            global max_selects
            max_selects = selects[:]  # 注意，这里需要用切片的方式，因为那边pop了，不然会是空的。
    else:
        # 第一种情况，不放。
        selects.append(0)
        search(depth+1, rest)
        selects.pop()
        # 第二种情况，放。
        if rest >= info[depth][0]:
            selects.append(1)
            search(depth + 1, rest - info[depth][0])
            selects.pop()


if __name__ == "__main__":
    search(0, 5)
    print(max_value)







