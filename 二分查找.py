def get_target(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1
#查找第一个不小于目标值的函数
def find_2(nums,target):
    left,right=0,len(nums)
    while left<right:
        mid=left+(right-left)//2
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid
    return right
#查找第一个大于目标值的数
def find_3(nums,target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right


