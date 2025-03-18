class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        count = 0
        for i in nums:
            if i == target:
                count += 1
        idx = nums.index(target)
        return [idx, idx+count-1]
