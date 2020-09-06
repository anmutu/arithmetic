# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/18 23:40

# https://leetcode-cn.com/problems/plus-one/

# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头

# example
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]


def plus_one(digits):
    """
    把数组转换成数字。
    数字+1
    然后转换回去
    """
    digits = [str(i) for i in digits]
    num = int("".join(digits))
    num += 1
    digits = [int(i) for i in str(num)]
    return digits


if __name__ == "__main__":
    digits = [4, 3, 2, 1]
    res = plus_one(digits)
    print(res)




# 已经两个链接表A为：1->2->3
# B :4->5->6
# 使之结果为9->7->5


