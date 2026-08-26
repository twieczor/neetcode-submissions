class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = {}
        h2 = {}

        if len(s) != len(t):
            return False        

        for c in s:
            h1[c] = h1[c] + 1 if c in h1 else 1

        for c in t:
            if c in h1:
                h1[c] -= 1
                if h1[c] < 0:
                    return False
            else:
                return False
        return True
            


