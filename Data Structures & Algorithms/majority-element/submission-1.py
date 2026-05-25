class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        res,maxCount = 0,0

        for n in nums:
            hash_map[n] = hash_map.get(n,0)+1

            res = n if hash_map[n] > maxCount else res
            maxCount = max(hash_map[n],maxCount)
        return res