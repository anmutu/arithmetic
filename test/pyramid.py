# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/8/7 1:40

pyramid = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

# dp。分解，一步一步的去做的。
# 自底向上的一个过程。
# 无后效性的。



# 第一步是把倒数第二行变身 [4, 5, 6],

if __name__ == "__main__":
    for j in range(3, 0, -1):
        for i in range(j):
            pyramid[j-1][i] += max(pyramid[j][i], pyramid[j][i + 1])
    print(pyramid[0])



    # for i in range(3):
    #     print("要变身的值是:", pyramid[2][i])
    #     print("下左的值是:", pyramid[3][i])
    #     print("下右的值是:", pyramid[3][i+1])
    #     pyramid[2][i] += max(pyramid[3][i], pyramid[3][i+1])
    #     print("要变身的值是:", pyramid[2][i])
    #     print(pyramid[2])
    #     print("+++++++++")
    #
    # for i in range(2):
    #     print("")
    #     print("要变身的值是:", pyramid[1][i])
    #     print("下左的值是:", pyramid[2][i])
    #     print("下右的值是:", pyramid[2][i + 1])
    #     pyramid[1][i] += max(pyramid[2][i], pyramid[2][i + 1])
    #     print("要变身的值是:", pyramid[1][i])
    #     print(pyramid[1])
    #     print("+++++++++")
    #
    # for i in range(1):
    #     print("")
    #     print("要变身的值是:", pyramid[0][i])
    #     print("下左的值是:", pyramid[1][i])
    #     print("下右的值是:", pyramid[1][i + 1])
    #     pyramid[0][i] += max(pyramid[1][i], pyramid[1][i + 1])
    #     print("要变身的值是:", pyramid[0][i])
    #     print(pyramid[0])
    #     print("+++++++++")






