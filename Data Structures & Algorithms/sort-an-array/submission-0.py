class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []

        for num in range(min(nums), max(nums) + 1):
            if num in count:
                for _ in range(count[num]):
                    result.append(num)

        return result
