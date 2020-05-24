# _*_ coding :utf-8 _*_
__author__ = 'du'
__github__ = 'www.github.com/anmutu;'
__date__ = '2020/5/18 19:34'

# https://leetcode-cn.com/problems/contains-duplicate/

# 给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

# example
# 输入: [1,2,3,1]
# 输出: true


def is_contains_duplicate(nums):
    """用set这个去取巧得到想要的结果"""
    if len(nums) == len(set(nums)):
        return True
    else:
        return False


def is_contains_duplicate1(nums):
    """
    思路就是第i个元素是否in在i后面的元素里。
    """
    for i in range(len(nums)-1):  # 注意这里的边界，好好是-1
        if nums[i] in nums[i+1:]:  # 也要注意这里的边界，最开始就忘了+1，测试出来了
            return False
        return True


def is_contains_duplicate2(nums):
    """
    sort之后 就比较相邻的两个是否相同了
    """
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return False
        else:
            return True


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    flag = is_contains_duplicate(nums)
    print(flag)

    flag1 = is_contains_duplicate1(nums)
    print(flag1)

    flag2 = is_contains_duplicate2(nums)
    print(flag2)

    nums1 = [1, 2, 3, 4]
    flag4 = is_contains_duplicate(nums1)
    print(flag4)

    flag5 = is_contains_duplicate1(nums1)
    print(flag5)

    flag6 = is_contains_duplicate2(nums1)
    print(flag6)




