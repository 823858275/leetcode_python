#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                left=i-1
                break
            if i==1:
                nums.reverse()
                return
        for i in range(len(nums)-1,left,-1):
            if nums[i]>nums[left]:
                right=i
                break
        nums[left],nums[right]=nums[right],nums[left]
        a=nums[left+1:]
        a.reverse()
        nums[left+1:]=a

a=[1,3,2]
a=a[::-1]
#Solution().nextPermutation(a)
print(a)