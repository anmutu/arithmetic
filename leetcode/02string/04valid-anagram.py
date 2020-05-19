# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/19 22:42

# https://leetcode-cn.com/problems/valid-anagram/

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# example
# 输入: s = "anagram", t = "nagaram"
# 输出: true


def is_anagram(s, t):
    """
    思路：将其转换成list然后排序，
    接着一个一个比较，如果相等，就比较下一个。
    如果不相等就说明不是字母异位词。
    """
    if len(s) != len(t):
        return False
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    for i in range(len(s)):
        if s_list[i] == t_list[i]:
            continue
        else:
            return False
    return True


if __name__ =="__main__":
    s = "anagram"
    t = "nagaram"
    res = is_anagram(s, t)
    print(res)

    s1 = "rat"
    t1 = "car"
    res1 = is_anagram(s1, t1)
    print(res1)






