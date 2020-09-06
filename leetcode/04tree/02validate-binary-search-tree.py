# @Author    : 小杜同学
# @Email       : anmutu@hotmail.com
# @Github     : www.github.com/anmutu
# @怎么肥四  : https://www.zmfei4.com
# @Time        : 2020/5/20 22:19

# https://leetcode-cn.com/problems/validate-binary-search-tree/

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# example
# 输入:
#     2
#    / \
#   1   3
# 输出: true


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_binary_search_tree(self, root):
        import sys
        min = sys.maxsize*(-1)
        max = sys.maxsize
        return self.is_binary_search_tree()

    def valid_bst(self, root, left, right):
        if root == None:
            return False
        if root.val < min or root.val > max:
            return False

