class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        

        if 0 == n:
            return 0
        if 1 == n:
            return nums[0]

        #input: 5,4,-1,7,8
        #5
        #5+4 4
        #9+-1 4+-1 -1
        #8+7  3+7  -1+7 7
        #15+8 10+8 6+8  7+8 8
        #23   18   14   15  8

        #output is 23
        
        #assign top of the pyramid so we can start from the second row
        #range(1,n) and not to worry about end-1 lower than zero        
        dp[0][0] = nums[0]
        ret = dp[0][0]

        for end in range(1, n):
            for start in range(0, end +1):
                dp[end][start] = nums[end] + dp[end-1][start]
                ret = max(dp[end][start], ret)
                #print(dp[start][end])
            #print(dp[end])

        

        return ret