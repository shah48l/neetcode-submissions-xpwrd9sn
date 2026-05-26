from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        for n in s:
            freq[n] += 1 
        
        for n in t:
            freq[n] -=1

        for values in freq.values():
            if values != 0:
                return False 

        return True