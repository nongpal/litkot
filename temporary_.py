class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        idx = 1

        while idx <= len(nums):
            initial = nums[idx-1]
            if initial in nums[idx:]:
                return True
            idx += 1
        return False
        # return False if len(set(nums)) == len(nums) else True <- (solusi cheater)
