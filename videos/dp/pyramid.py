# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/8/7 17:09


pyramid = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

# 第一步，把  [4, 5, 6],变身，也就是找到这一层的最优解。
# 第二步，把 [2, 3],变身，找到这一层的最优解。
# 第三步，   [1],变身，找到这一层的最优解。


if __name__ == "__main__":
    for j in range(3, 0, -1):
        for i in range(j):
            pyramid[j-1][i] += max(pyramid[j][i], pyramid[j][i + 1])
    print(pyramid[0][0])



    # for i in range(3):
    #     print("变身前的数:", pyramid[2][i])
    #     print("左下值的数:", pyramid[3][i])
    #     print("右下值的数:", pyramid[3][i+1])
    #     pyramid[2][i] += max(pyramid[3][i], pyramid[3][i+1])
    #     print("变身后的数:", pyramid[2][i])
    #     print("++++++++++++++++++++++++++")
    # print(pyramid[2])
    #
    # print("")
    # for i in range(2):
    #     print("变身前的数:", pyramid[1][i])
    #     print("左下值的数:", pyramid[2][i])
    #     print("右下值的数:", pyramid[2][i+1])
    #     pyramid[1][i] += max(pyramid[2][i], pyramid[2][i+1])
    #     print("变身后的数:", pyramid[1][i])
    #     print("++++++++++++++++++++++++++")
    # print(pyramid[1])
    #
    # print("")
    # for i in range(1):
    #     print("变身前的数:", pyramid[0][i])
    #     print("左下值的数:", pyramid[1][i])
    #     print("右下值的数:", pyramid[1][i+1])
    #     pyramid[0][i] += max(pyramid[1][i], pyramid[1][i+1])
    #     print("变身后的数:", pyramid[0][i])
    #     print("++++++++++++++++++++++++++")
    # print(pyramid[0])
    #
    #
