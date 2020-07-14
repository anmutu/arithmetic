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

# 删除追加法
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


#  双指针方法
#  定义一个left指针，它负责统计数据为0的元素。
#  定义一个right指针，它负责统计所有的数据。
#  遍历数组，终结条件为right指针到了最后一个数。
#  起始条件left和right都为0.
#  当left指针遇到了0时，则将left到倒数第二个元素之间的元素，放到最前面，最后一个元素设置为0，且将right指针+1.
#  当left指针没有遇到0时，则将left和right指针都+1
#  事实上每一次遍历right指针都会往后移动，只是如果left指针遇到了0，则要做一个类似把0移动到最后位置去的一个操作。

def move_zeros1(nums):
    left = 0
    right = 0
    while right < len(nums)-1:
        if nums[left] == 0:
            nums[left:-1] = nums[left+1:]
            nums[-1] = 0
            right += 1
        else:
            left += 1
            right += 1
    return


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    print(nums)

    move_zeros1(nums)
    print(nums)

