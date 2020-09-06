# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/8/7 16:14

pyramid = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10]
]

# 第一步，把   [4, 5, 6]去做变身。
# 第二步，在上面的基础上 对[2, 3],进行变身。
# 第三步，在上面基础上对  [1]变身。


if __name__ == "__main__":
    for i in range(3):
        print("变身前的值是", pyramid[2][i])
        print("下左值是", pyramid[3][i])
        print("下右值是", pyramid[3][i+1])
        pyramid[2][i] += max(pyramid[3][i], pyramid[3][i+1])
        print("变身后的值是", pyramid[2][i])
