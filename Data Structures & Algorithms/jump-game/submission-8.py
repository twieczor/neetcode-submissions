class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n < 1:
            return False
        if n < 2: return True

        l,r = 0,0
        while l <= r and r < n:
            k = nums[l]
            if l + k > r:
                r = l + k
            l += 1
        return r >= n-1

        