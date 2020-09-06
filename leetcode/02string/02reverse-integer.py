# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/19 20:33

# https://leetcode-cn.com/problems/reverse-integer/

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# example
# 输入: -123
# 输出: -321
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。

# 现在用字符串代码完成了这个题目，其实还可以用数学的方法。


def reverse(x):
    """
    字符串解法代码：
    先将数字类型的x转换成列表
    然后后切片方式拿到想要的结果
    要特别注意：切片的使用。r_list[1:][::-1]。
    """
    r_list = list(str(x))   # 转换成list
    if r_list[0] == "-":
        num = int(''.join(r_list[1:][::-1])) * (-1)  # 从下标为1的开始反转，然后*-1
    else:
        num = int(''.join(r_list[::-1]))   # 是正数就从下标为0的开始反转就好

    if num in range(pow(2, 31)*(-1), pow(2, 31)-1):
        return num
    else:
        return 0


if __name__ == "__main__":
    print("现在是数字是负数的情况：")
    n = -123
    res = reverse(n)
    print(res)

    print("现在是数字超出取值范围的情况：")
    n1 = pow(2, 31)
    res1 = reverse(n1)
    print(res1)
