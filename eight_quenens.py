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
    # 第四步，判断“\"方向是否有皇后
    for index, i in enumerate(range(x - 1, -1, -1)):
        q_y = y - (index + 1)
        if q_y >= 0:
            if chessboard[i][q_y] == 1:
                return False
    return True


def print_chessboard():
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 0:
                print("q ", end=" ")
            else:
                print("* ", end=" ")
        return print()



def put_queen(step):
    if step == 8:
        print_chessboard()
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        return
    for i in range(8):
        if valid(step, i):
            chessboard[step][i] == 1
            put_queen(step + 1)
            chessboard[step][i] == 0


if __name__ == "__main__":
    print_chessboard()
    # put_queen(0)
