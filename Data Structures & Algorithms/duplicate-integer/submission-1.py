class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = 0
        nums.sort()
        for r in range(1,len(nums)):
            if nums[l] == nums[r]:
                return True 
            else:
                l+=1
        return False