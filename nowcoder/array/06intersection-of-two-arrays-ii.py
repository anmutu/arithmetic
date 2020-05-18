# _*_ coding :utf-8 _*_
__author__ = 'du'
__github__ = 'www.github.com/anmutu;'
__date__ = '2020/5/18 21:44'


# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

# 给定两个数组，编写一个函数来计算它们的交集.

# example
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]


def intersect(nums1, nums2):
    """
    就是两组数排序后
    用第一组的第一个数分别去比第二组 数的第一个
    谁小则谁的位置往后移动一位，再去做比较。
    如果两个数一样大，那么就需要将这个数加入到我们的结果集中，且两组要比较的数都往后移一位。
    """
    nums1.sort()
    nums2.sort()
    r_list = []
    p1 = 0
    p2 = 0
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] == nums2[p2]:
            r_list.append(nums1[p1])
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    return r_list


def intersect1(nums1, nums2):
    """
     这种情况是适用于nums1和nums2的长度相差很多。
     我们用较短的nums里的每个元素和长的nums去做比较。
     如果较长的里面有，则将这个元素加入到我们的结果集
     且把这个元素从较长的数组里remove,
     接着继续用较短的nums去比较较长的nums
    """
    nums1.sort()
    nums2.sort()
    r_list = []
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    for n in nums1: # 这里用 for ... in ...
        if n in nums2:
            r_list.append(n)
            nums2.remove(n)
    return r_list


if __name__ == "__main__":
    print("第一种解法:")
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    res = intersect(nums1, nums2)
    print(res)

    print("第二种解法:")
    res1 = intersect1(nums1, nums2)
    print(res1)








