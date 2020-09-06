# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/21 17:09

# https://leetcode-cn.com/problems/first-bad-version/

# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

# example
# 给定 n = 5，并且 version = 4 是第一个错误的版本。
# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5) -> true
# 调用 isBadVersion(4) -> true
# 所以，4 是第一个错误的版本。


def first_bad_version(nums):
    left = 1
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if is_bad_version(mid):
            if is_bad_version(mid - 1):
                right = mid
            else:
                return mid
        else:
            if is_bad_version(mid + 1):
                return mid + 1
            else:
                left = mid


def is_bad_version(num):
    if num == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = first_bad_version(nums)
    print(res)

