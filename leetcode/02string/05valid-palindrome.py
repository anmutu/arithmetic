# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/20 2:45

# https://leetcode-cn.com/problems/valid-palindrome/

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。

# example
# 输入: "A man, a plan, a canal: Panama"
# 输出: true

# 这里还可以说用双指针的办法去做一下实现


def is_palindrome(str):
    """
    去除掉非字母的元素。
    然后以元素数量的中间的前半部分和后半部分去对比。
    如果前半部分和后半部分的反转部分一样则说明是回文串了。
    要注意”s_list[::-1][:n]“的写法。
    """
    if len(str) < 2:
        return True
    s_list = []
    str = str.lower()
    for word in str:
        if word.isalnum():
            s_list.append(word)

    n = len(s_list)//2
    if s_list[:n] == s_list[::-1][:n]:  # 注意这里的写法
        return True
    else:
        return False


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    res = is_palindrome(s)
    print(res)

    s1 = "huawei tencent"
    res1 = is_palindrome(s1)
    print(res1)



