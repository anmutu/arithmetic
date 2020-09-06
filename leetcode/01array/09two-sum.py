# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/19 2:37


# https://leetcode-cn.com/problems/two-sum/

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# example
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

def two_sum_wrong(nums, target):
    for i in nums:
        for j in nums:
            if i + j == target:
                return [i, j]


def two_sum(nums,  target):
    """
    遍历2次此数组。
    第一次range取所有。
    第二次取当前遍历元素后面的所有元素。一步一步缩小范围。
    看两者相加能不能得到目标值。
     特别注意：第二次遍历的range不能是len(nums)-1
     如数组是[4, 4, 5, 8],target是8的时候就会出一个错的结果。
    """
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):  # 这里不能range(len(nums))，
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum1(nums, target):
    for i in range(len(nums)-1):
        if target - nums[i]  in nums[i+1:]:
            j = nums[i+1:].index(target - nums[i])
            return [i, i +j+1]


if __name__ == "__main__":
    print("错误的求法：")
    nums = [2, 7, 11, 15]
    target = 9
    res = two_sum_wrong(nums, target)
    print(res)

    print("正确的求法1：")
    res1 = two_sum(nums, target)
    print(res1)

    print("正确的求法2：")
    res2 = two_sum(nums, target)
    print(res2)

