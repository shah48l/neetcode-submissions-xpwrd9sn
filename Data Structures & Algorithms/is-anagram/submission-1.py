class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i],0) + 1 
            t_hash[t[i]] = t_hash.get(t[i],0)+1

        for c in s_hash:
            if s_hash[c] != t_hash.get(c,0):
                return False
        return True