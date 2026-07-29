class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 2:
            return n

        nums.sort()

        ret = 0
        cnt = 1

        for i in range(1, n):
            diff = nums[i]-nums[i-1]

            if diff == 1:
                cnt += 1
            elif diff > 1:
                ret = max(ret, cnt)
                cnt = 1

        ret = max(ret, cnt)
        return ret

