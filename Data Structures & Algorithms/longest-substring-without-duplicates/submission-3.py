class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        max_w = 0
        sett = set()

        while r<len(s):
            if s[r] not in sett:
                sett.add(s[r])
                max_w = max(max_w,(r-l)+1)
                r+=1
            else:
                sett.remove(s[l])
                l+=1
        return max_w