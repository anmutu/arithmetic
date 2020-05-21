# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/21 19:06

# https://leetcode-cn.com/problems/climbing-stairs/

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# example
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶


def climb_stairs(n):
    """
     发现规律：总步数与台阶数是一个fib数列。
    """
    step_list = [1, 1, 2]
    i = n
    while  2 < i:
        step_list.append(step_list[-1] + step_list[-2])
        i -= 1
    return step_list[n]


if __name__ == "__main__":
    for i in range(10):
        print(climb_stairs(i))











