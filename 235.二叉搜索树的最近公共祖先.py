#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pa=min(p.val,q.val)
        pb=max(p.val,q.val)
        return self.findNode(root,pa,pb)
    def findNode(self,node: TreeNode,a: int,b: int):
        if not node:
            return None
        tmp=node.val
        if tmp>=a and tmp<=b:
            return node
        elif tmp<a:
            return self.findNode(node.right,a,b)
        elif tmp>b:
            return self.findNode(node.left,a,b)
        

