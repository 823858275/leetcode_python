#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
#滑动窗口，双指针，建立一个哈希表，key为字符，value为对应的索引
#不停移动右指针，当哈希表中存在重复元素，移动左指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        dic = {}
        max_length = float("-inf")      #存放最大的长度
        while left < len(s) and right < len(s):#开始遍历
            if dic.get(s[right]) is not None:#当滑动窗口内存在重复的元素
                max_length = max(max_length,right-left)#修改最大的长度
                left = max(dic[s[right]]+1,left)        #移动左指针
                dic[s[right]]=right                     #修改哈希表对应的元素
            else:
                dic[s[right]] = right               #当晃动窗口不存在重复的元素，将该元素添加到哈希表中
            right += 1
        max_length=max(max_length,right-left)       #判读一下最后的情况
        return max_length
