#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n=len(nums)
        return self.recursion(nums,0,n-1)
    def recursion(self,nums: List[int],l: int,r: int) -> TreeNode:
        if l>r:
            return None
        m=(l+r)//2
        node=TreeNode(nums[m])
        node.left=self.recursion(nums,l,m-1)
        node.right=self.recursion(nums,m+1,r)
        return node
