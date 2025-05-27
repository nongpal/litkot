class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if n + extraCandies >= max(candies) else False for n in candies]
