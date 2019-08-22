#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        left=0
        right=x
        while left<right:
            mid=left+(right-left)//2
            s=mid*mid
            if s<=x:
                left=mid+1
            else:
                right=mid
        return right-1



