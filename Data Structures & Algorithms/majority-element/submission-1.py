class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        check = {}
        for num in nums:
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        
        check = sorted(check, key=check.get, reverse=True)
        return check[0]