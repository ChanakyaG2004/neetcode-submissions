class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}
        for i, num in enumerate(nums):
            if target - num not in check:
                check[num] = i
            else:
                return [check[target-num], i]
        
