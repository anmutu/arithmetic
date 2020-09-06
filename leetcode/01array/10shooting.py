# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/7/11 1:55

#  现在有一个人对一堆数量为n个的气球射击，假设气球的颜色为m种。
#  要求求出把射中所有球的最短的连续的数列。
#  假设射中情况是[0, 1, 2, 0, 1, 2, 3, 1, 2, 2, 3, 4],其中0表示没有射中任何气球,其他数字表示的是一种颜色的气球。

# example
# [0, 1, 2, 0, 1, 3, 2,  1, 2, 2, 3, 4, 4, 2, 1, 1, 2, 3,0]
# [1, 2, 2, 3, 4]



#
# def shooting(nums):
#     r = [[]]
#     index = []
#     length = len(list(set(nums))) - 1
#     if len(nums) < length:
#         return False
#     res = []
#     for i in range(length):
#         if nums[i] not in res:
#             res.append(nums[i])
#             if len(res) == length:
#                 return res
#     for i in range(len(nums)-1):
#         if nums[i] == 0:
#             index.append(i)
#
#     for i in range(len(index)):
#         a =

    #
    # return index

# 遍历数组
# 1.如果当前数不为0则将之加入到新数组n
# 2.如果遇到当前的是0
# 2.1则判断之前的数组n的长度是否小于颜色数，如果小于则将数组清空
# 2.2如果当前数组的长度是大于等于颜色数，则将之放到一个二维的数组中


def shooting1(nums):
    n = []
    ns = [[]]
    length = len(list(set(nums)))-1
    for i in range(len(nums)):
        if nums[i] != 0  :
            n.append(nums[i])
            if i == len(nums)-1:
                ns.append(n)
        else:
            if len(n) < length:
                n = []
            else:
                ns.append(n)

    for i in range(len(ns)):
        if len(list(set(ns[i]))) == length:
            return ns[i]


# def shooting(nums):
#     length = len(list(set(nums)))-1
#     left = 0
#     right = 0
#     for i in range(len(nums)-1):
#         if nums[right] == 0:
#             if len(list(set(nums[left+1:right]))) != length:
#                 left = i
#             else:
#                 return nums[left+1:right]
#         right += 1
#


# def shooting(nums):
#     length = len(list(set(nums)))-1
#     left = 0
#     right = 0
#     while right == len(nums)-1:
#         if nums[left] == 0:
#


# def shooting(nums):
#     length = len(list(set(nums)))-1
#     if len(list(set(nums[:length]))) == length:
#         return nums[:length]
#     for i in range(length, len(nums)-1):
#         if len(list(set(nums[:length]))) and 0  not in nums[:length] == length:
#             return nums[:length]
#         else:


def shooting(nums):
    length = len(list(set(nums))) - 1
    res = []
    for i in range(len(nums)):
        if nums[i] != 0:
            res.append(nums[i])
            if len(list(set(res))) == length:
                return res
        else:
            if len(list(set(res))) == length:
                return res
            else:
                res = []
    if len(list(set(res))) == length:
                return res



if __name__ == "__main__":
    nums = [0, 1, 0, 2, 0, 2, 1, 2, 1, 0, 1]
    print(shooting(nums))

    nums1 = [0, 1, 0, 2, 0, 2, 1, 2, 1, 0, 3]
    print(shooting(nums1))

    nums2 = [0, 1, 0, 2, 0, 2, 1, 2, 1, 0, 3, 3, 1, 2]
    print(shooting(nums2))




