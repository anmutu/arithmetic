# _*_ coding :utf-8 _*_
__author__ = 'du'
__github__ = 'www.github.com/anmutu;'
__date__ = '2020/5/18 15:28'

# 删除重复元素

# 要求时间复杂度为O(1)


def remove_duplicates(nums):
    """
    如果第一个元素和第二个元素相等
    则用切片的方式把第二个元素放到最后
    第三个及后面的元素以切片的方式给到第二个及其后面的元素
    遍历次数为数组集合的数量
    """
    n = len(set(nums))
    i = 0
    while i < n-1:
        if nums[i] == nums[i+1]:
            temp = nums[i+1]
            nums[i+1:len(nums)-1] = nums[i+2:]
            nums[-1] = temp
            print(nums)
            continue
        else:
            i += 1
    return n


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [1, 1, 3, 5, 5, 8]
    remove_duplicates(nums1)
    remove_duplicates(nums2)






