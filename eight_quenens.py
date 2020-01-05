# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/3 1:05'

chessboard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def valid(x, y):
    # 判断x,y坐标能否放皇后
    # 第一步,判断x行是否有皇后
    for i in range(0, y):
        if chessboard[x][i] == 1:
            return False
    # 第二步,判断y列是否有皇后
    for i in range(0, x):
        if chessboard[i][y] == 1:
            return False
    # 第三步,判断"/"方向上是否有皇后,规律:这个点的攻击范围的下标相加,也就是x和y相加都是相同的.
    for i in range(0, x):
        if x + y - i <= 7:
            if chessboard[i][x - y - i] == 1:
                return False
