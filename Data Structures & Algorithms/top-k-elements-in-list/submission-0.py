class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = defaultdict(int)
        for i in nums:
            values[i]+=1
     
        sorted_nums = sorted(values, key=lambda x: values[x], reverse=True)
        answer = sorted_nums[:k]
            
        return answer