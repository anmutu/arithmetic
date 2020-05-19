# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/20 3:24

# https://leetcode-cn.com/problems/implement-strstr/

# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。

# example
# 输入: haystack = "hello", needle = "ll"
# 输出: 2


def str_str(haystack, needle):
    """
    思路就是在haystack里，从其第一个元素往后取nddele的长度的串跟needle比较。
    如果不同，则往后移一位，一样取同样长度的串与needle比较。
    一旦相同，则返回当前的这个移动的p。
    注意：下面注释的这个range的临界值是要+1的。没注释的while条件也不能少了”=”。
    总的原因就是range不包括临界值的和能移动的最大步数也应该包含进来。
    """
    if len(haystack) < len(needle):
        return
    if haystack == needle:
        return 0
    p = 0
    length = len(needle)
    # for i in range(len(haystack) - len(needle)+1):
    #     if haystack[p:p+length] == needle:
    #         return p
    #     else:
    #         p += 1
    step = len(haystack) - len(needle)
    while p <= step:
        if haystack[p:p+length] == needle:
            return p
        else:
            p += 1
    return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    res = str_str(haystack, needle)
    print(res)

    haystack1 = "abcd520"
    needle1 = "520"
    res1 = str_str(haystack1, needle1)
    print(res1)


