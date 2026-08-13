class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #123456
        #612345
        #561234
        #456123
        #345612
        #234561

        def bin_search(arr, t):
            #print(arr)



            l,r = 0, len(arr)-1

            while l <= r:
                m = l + (r - l)//2

                #012

                if arr[m] == t:
                    return m
                elif t < arr[m]:
                    r = m - 1
                else:
                    l = m + 1
            return -1


        n = len(nums)

        if n < 1:
            return -1
        elif n < 2:
            return 0 if target == nums[0] else -1

        l,r = 0, n - 1

        if nums[l] < nums[r]:
            #single range
            #binary search target

            return bin_search(nums, target)

        else:
            #two ranges

            #binary search border
            while l <= r:
                m = l + (r - l)//2

                if nums[m] == target:
                    return m

                if nums[m] > nums[m + 1]:
                    #found rotation point
                    if nums[0] <= target:
                        off = bin_search(nums[0:m], target)
                        return off
                    else:
                        off = bin_search(nums[m+1:], target)
                        return -1 if off == -1 else off + m + 1

                    
                elif nums[0] > nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
                    


            #binary search target


