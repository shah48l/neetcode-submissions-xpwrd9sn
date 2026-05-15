class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        for r in range(1,len(numbers)-1):
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            else:
                l+=1
        return []