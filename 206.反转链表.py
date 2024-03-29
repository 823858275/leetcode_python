#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curNode=head
        preNode=None
        while curNode:
            nextNode=curNode.next
            curNode.next=preNode
            curNode=nextNode
        return 

