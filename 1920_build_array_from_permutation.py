class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idx = 0
        ans = [0 for _ in range(n)] # create zeros array
        while idx < n:
            ans[idx] = nums[nums[idx]]
            idx += 1
        return ans
