# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/8/21 14:10




# 00 01 02
# 10 11 12
# 20 21 22

# 20 10 00
# 21 22 01
# 00 01 02

if __name__ == "__main__":

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix = [[col for col in range(4)] for raw in range(4)]

    print(len(matrix))
    print(matrix)

    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            print("f:", i, j, matrix[i][j])
            print("s:", j, i, matrix[j][i])
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print("+++++++")
    print(matrix)

    # for i in range(len(matrix)):
    #     matrix[i].reverse()
    # print(matrix)








