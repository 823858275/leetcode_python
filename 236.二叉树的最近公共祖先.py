#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p=[]
        path_q=[]
        self.findPath(root,path_p,p)
        self.findPath(root,path_q,q)
        i=0
        while i<len(path_p) and i<len(path_q):
            if path_p[i]!=path_q[i]:
                return path_p[i-1]
            i+=1
        if i==len(path_p):
            return path_p[-1]
        if i==len(path_q):
            return path_q[-1]
    def findPath(self,root: TreeNode,path: List,node: TreeNode) -> bool:
        if not root:
            return False
        if root==node:
            path.append(root)
            return True
        path.append(root)
        l=left=self.findPath(root.left,path,node)
        r=right=self.findPath(root.right,path,node)
        if l or r:
            return True
        path.pop()
        return False

