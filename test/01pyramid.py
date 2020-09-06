# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/7/21 9:30


pyramid = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]


if __name__ == "__main__":
    # [4,5,6]变身。第一步把倒数第二行的数据转换成全新的数据。即把[4,5,6]转换成全新的数据。
    for i in range(3):
        print("变身前的值为:", pyramid[2][i])
        print("下左的值为:", pyramid[3][i])
        print("下右的值为:", pyramid[3][i + 1])
        pyramid[2][i] += max(pyramid[3][i], pyramid[3][i+1])
        print("变身后的值为:", pyramid[2][i])
        print("++++++++++++++")
    print(pyramid[2])

# [2,3]变身
    print("")
    for i in range(2):
        print(pyramid[1][i])
        print(pyramid[2][i])
        print(pyramid[2][i + 1])
        pyramid[1][i] += max(pyramid[2][i], pyramid[2][i+1])
        print(pyramid[1][i])
        print("++++++++++++++")
    print(pyramid[1])

    # [1]变身
    print("")
    for i in range(1):
        print(pyramid[0][i])
        print(pyramid[1][i])
        print(pyramid[1][i + 1])
        pyramid[0][i] += max(pyramid[1][i], pyramid[1][i+1])
        print(pyramid[1][i])
        print("++++++++++++++")
    print(pyramid[0])



    for j in range(3, 0, -1):
        for i in range(j):
            # pyramid[2][i] += max(pyramid[3][i], pyramid[3][i + 1])
            pyramid[j - 1][i] += max(pyramid[j][i], pyramid[j][i + 1])
    print(pyramid[0][0])









