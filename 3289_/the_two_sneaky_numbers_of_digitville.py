class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        tmp = set()
        return [x for x in nums if (x in tmp or tmp.add(x))]
