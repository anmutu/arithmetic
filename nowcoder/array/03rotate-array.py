# _*_ coding :utf-8 _*_
__author__ = 'du'
__github__ = 'www.github.com/anmutu;'
__date__ = '2020/5/18 17:27'


# 旋转数组
# https://leetcode-cn.com/problems/rotate-array/
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# example
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]


def rotate_array1(nums, k):
    """取巧的方法，反转list后，用pop取反转后的第一个元素，加之append到数据中，最后再反转。"""
    if len(nums) < 2:
        return
    reversed(nums)
    # k = k % len(nums)
    # while k > 0:
    for i in range(k):
        temp = nums.pop(0)
        nums.append(temp)
        k -= 1
        print(nums)
    # reversed(nums)
    return


def rotate_array2(nums, k):
    if len(nums) < 2:
        return
    for i in range(k):
        temp = nums[-1]
        nums[1:] = nums[:-1]
        nums[0] = temp
        print(nums)
    return


def rotate_array3(nums, k):
    if len(nums) < 2:
        return
    temp = nums[len(nums)-k:]
    nums[k+1:] = nums[0:len(nums)-k]
    nums[0:k+1] = temp
    print(nums)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("reverse pop append 取巧方法解决：")
    rotate_array1(nums1, k)

    nums2 = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("一个一个交换解决：")
    rotate_array2(nums2, k)

    nums3 = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("整体交换解决：")
    rotate_array3(nums3, k)




