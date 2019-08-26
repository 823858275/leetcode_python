#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
#当出现重复的情况复杂度由logn退化为n
#当nums[0]与nums[mid]相等时需要依次遍历
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[0] == nums[mid]:
                return self.normSearch(nums)
            if nums[0] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    def normSearch(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]
