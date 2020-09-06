# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/7 2:10'

"""
用动态规划的方法解决金字塔求最大值的问题.
动态规划法是自底向上的一个操作,从最下面的值与上一层的值相加得到最大的值,一步一步如此向塔顶取值.
每用完一层,这一层就没有用了.也就是无后效性.
"""


pyramid = [
    [1],
    [2, 3],
    [4, 5, 6]
]

# 得到第1(索引)层的新值,需要得到新的两个值.
for i in range(2):
    pyramid[1][i] += max(pyramid[2][i], pyramid[2][i+1])
print("思路代码.用最下面一层与倒数第二层组合和到最大的值:{0}".format(pyramid[1]))

for i in range(1):
    pyramid[0][i] += max(pyramid[1][i], pyramid[1][i+1])
print("思路代码.用倒数第二层与它的上一层组合和到最大的值,这里也就是最终结果:{0}".format(pyramid[0]))


for i in range(2, 1, -1):
    for j in range(i):
        pyramid[i-1][j] += max(pyramid[i][j], pyramid[i][j+1])
        print(pyramid)
print("新的金字塔是{0},其最后的值是{1}".format(pyramid, pyramid[0][0]))


def search(depth):

    pyramid = [
        [1],
        [2, 3],
        [4, 5, 6]
    ]

    while depth >= 1:
        for row in range(0, depth):
            pyramid[depth - 1][row] += max(pyramid[depth][row], pyramid[depth][row+1])
        print(pyramid[j])
        depth -= 1


if __name__ == "__main__":
    search(2)







