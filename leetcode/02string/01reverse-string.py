# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/19 3:08

# https://leetcode-cn.com/problems/reverse-string/

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

# example
# 输入：["h","e","l","l","o"]
# # 输出：["o","l","l","e","h"]


def reverse_string(str):
    """
   遍历长度为长度的一半。
   然后用第一个和最后一个交换，以此类推。
    """
    length = len(str)
    if length < 2:
        return
    for i in range(length//2):
        str[i], str[length-1-i] = str[length-1-i], str[i]
        print(str)
    return str


def reverse_string1(str):
    str.reverse()
    return


if __name__ == "__main__":
    print("交换解决：")
    str = ["h", "e", "l", "l", "o"]
    res = reverse_string(str)
    print(res)

    print("用reverse()函数解决：")
    str1 = ["h", "e", "l", "l", "o"]
    reverse_string1(str1)
    print(str1)



