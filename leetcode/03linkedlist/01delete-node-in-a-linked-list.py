# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/20 18:38

# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/

# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

# example
# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def del_node(node: ListNode):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == "__main__":
    head = [4, 5, 1, 9]
    del_node()