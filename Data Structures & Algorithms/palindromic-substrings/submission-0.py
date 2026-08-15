class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        ret = 0

        for i in range(n):

            #i is center
            k = 0
            while i - k >= 0 and i + k < n:
                if s[i - k] != s[i + k]:
                    break
                ret += 1
                k += 1

            #i is side by side
            k = 0
            j = i + 1
            while i - k >= 0 and j + k < n:
                if s[i - k] != s[j + k]:
                    break
                ret += 1
                k += 1 

        return ret

            

            