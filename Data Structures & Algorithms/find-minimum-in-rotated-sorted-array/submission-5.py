class Solution:
    def findMin(self, nums: List[int]) -> int:

        #561


        def is_min(x, nums):
            left,right = 0,0
            if x == 0:
                left = len(nums) - 1
            else:
                left = x - 1
            if x == len(nums) - 1:
                right = 0
            else:
                right = x + 1

            return nums[left] > nums[x] < nums[right]
        
        n = len(nums)

        if n < 2:
            return nums[0]
        elif n < 3:
            return min(nums[0], nums[1])

        l,r = 0,n - 1
        mid = 0

        while l<=r:
            mid = l + (r - l) // 2

            if is_min(mid, nums):
                return nums[mid]
            elif nums[mid] > nums[n-1]:
                l = mid + 1
            else:
                r = mid - 1
        return left
        


        