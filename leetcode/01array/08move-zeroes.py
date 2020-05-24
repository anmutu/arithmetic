# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/19 2:27


# https://leetcode-cn.com/problems/move-zeroes/

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# example
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 还可以用双指针的方法去解决这个。

def move_zeros(nums):
    """
    删除追加法，简单粗暴。
    从第一个元素往后找，遇到0，则将这个元素删除，并在这个数组尾部append 一个0
    """
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    print(nums)

