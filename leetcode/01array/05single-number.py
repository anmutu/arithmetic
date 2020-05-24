# _*_ coding :utf-8 _*_
__author__ = 'du'
__github__ = 'www.github.com/anmutu;'
__date__ = '2020/5/18 20:03'

# https://leetcode-cn.com/problems/single-number/

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# example
# 输入: [4,1,2,1,2]
# 输出: 4


def single_number(nums):
    """思路：先排好序，然后每两个为一组的比较进而进行判断"""
    nums.sort()
    length = len(nums)
    if length < 3:
        return nums[0]
    i = 0
    while i < length-2:
        if nums[i] == nums[i+1]:
            i += 2  # 这里是两个两个比较，所以这里要加+2.
        else:
            return nums[i]
    return nums[-1]


def single_number1(nums):
    """
    排序后，找出偶数和奇数的set,让他们相减，然后取list的第一个就好
    注意nums[::2]这样的写法。表示从下标0开始2个2个的往后取值。
    """
    # nums.sort()
    # set1 = set(nums[::2])
    # set2 = set(nums[1::2])
    # r = list(set1 - set2)
    # print(r[0])
    nums.sort()
    n = list(set(nums[::2]) - set(nums[1::2]))[0]
    return n


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    res = single_number(nums)
    print(res)

    nums1 = [4, 1, 4, 1, 2]
    res1 = single_number(nums1)
    print(res1)

    print("用第二种方法实现：")
    nums = [4, 1, 2, 1, 2]
    res = single_number1(nums)
    print(res)

    nums1 = [4, 1, 4, 1, 2]
    res1 = single_number1(nums1)
    print(res1)




