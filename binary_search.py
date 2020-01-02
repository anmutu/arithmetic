# _*_ coding :utf-8 _*_
__author__ = 'du'
__blog__ = 'www.cnblogs.com/anmutu;www.zmfei4.com;'
__date__ = '2020/1/2 14:18'

data = [12, 123, 234, 345, 456, 567, 678, 789, 888, 999]


def search(data_list, target):
    left = 0
    right = len(data_list) - 1
    target_position = -1
    while left <= right:
        # 第一步，找到中间值
        mid = int((left + right) / 2)  # 索引下标需要是int类型的
        # 第二步，判断目标值与中间值之大小
        if target == data_list[mid]:
            target_position = mid
            break
        elif target > data_list[mid]:
            # 如果目标值大于中间值则说明目标值位于右侧
            left = mid + 1
        else:
            # 这里说明目标值小于中间值，则此时目标值位于左侧
            right = mid - 1
    return target_position


if __name__ == "__main__":
    pos = search(data, 888)
    if pos >= 0:
        print("查到数据，其位置位于:{}".format(pos))
    else:
        print("此数值并不位于当前数组中")
