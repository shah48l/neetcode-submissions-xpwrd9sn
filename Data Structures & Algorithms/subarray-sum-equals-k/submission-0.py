class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0

        prefix_hash = { 0: 1 }

        for n in nums:
            cursum += n 
            diff = cursum - k 

            res+= prefix_hash.get(diff,0)

            prefix_hash[cursum] = 1 + prefix_hash.get(cursum,0)

        return res