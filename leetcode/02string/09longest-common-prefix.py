# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/20 15:37

# https://leetcode-cn.com/problems/longest-common-prefix/

# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# example
# 输入: ["flower","flow","flight"]
# 输出: "fl"


def longest_common_prefix(strs):
    """
    遍历边界值为最短元素的长度
    接着就遍历这个列表，将当前列表中每个元素的第i个元素放入一个新列表中。
    利用set的特点判断这个新列表的长度是否为1，如果是1，则说明是一样的元素。
    如果不是，则说明在 当前i之前的就是公共的最长前缀了。
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    length = min([len(s) for s in strs])
    common_word = []
    for i in range(length):
        for word in strs:
            common_word.append(word[i])
        if len(set(common_word)) == 1:  # 说明当前元素是相同的
            common_word = []
        else:
            return strs[0][0:i]
    return 


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    res = longest_common_prefix(strs)
    print(res)



