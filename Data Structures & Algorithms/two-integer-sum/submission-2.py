class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counter = 0
        seen = {}

        for i,n in enumerate(nums):
            value = target - n
            if value in seen:
                return [seen[value], i]
            seen[n] = i

        return []