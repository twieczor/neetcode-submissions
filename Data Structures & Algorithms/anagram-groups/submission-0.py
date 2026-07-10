class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ht = {}

        for word in strs:
            print(word)
            ws = "".join(sorted(word))
            if ws in ht:
                ht[ws].append(word)
            else:
                ht[ws] = []
                ht[ws].append(word)
        
        ret = []
        for kp in ht:
            ret.append(ht[kp])

        return ret

            
        
        