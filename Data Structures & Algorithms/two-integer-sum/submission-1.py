class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for ind,val in enumerate(nums):
            complement = target - val 

            if complement in hash_map:
                return [hash_map[complement],ind]

            hash_map[val] = ind