# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/7/14 21:16

# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 你找到的子数组应是最短的，请输出它的长度。

# example
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
from typing import List


def find_unsorted(nums):
    diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
    return len(diff) and max(diff) - min(diff) + 1


def get_len(nums):
    new_nums = nums.sort()



if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    print(find_unsorted(nums))
