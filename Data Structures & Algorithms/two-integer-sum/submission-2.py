class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        if n < 2:
            return []

        ht = {}

        for i in range(n):
            diff = target - nums[i]
            if diff in ht:
                return [ht[diff], i]
            else:
                ht[nums[i]] = i

        return []
        
