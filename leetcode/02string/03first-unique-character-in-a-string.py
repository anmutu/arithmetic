# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/19 22:18

# https://leetcode-cn.com/problems/first-unique-character-in-a-string/

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# example
# s = "leetcode"
# 返回 0.


def first_unique_char(str):
    """
    这里也是用到了切片快速的解决了问题。
    当然还可以用哈希算法解决这个问题。
    """
    if len(str) < 2:
        return 0
    for i in range(len(str)):
        if str[i] not in str[i+1] and str[i] not in str[:i]:
            return i
    return -1


if __name__ == "__main__":
    str = "leetcode"
    res = first_unique_char(str)
    print(res)

