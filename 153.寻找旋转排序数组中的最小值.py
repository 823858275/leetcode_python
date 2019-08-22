#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 
        if len(nums)==1:
            return nums[0]
        l,r=0,len(nums)
        if nums[r]>nums[l]:
            return nums[l]
        while right>left:
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[0]:
                l=mid+1
            else:
                r=mid-1
                


