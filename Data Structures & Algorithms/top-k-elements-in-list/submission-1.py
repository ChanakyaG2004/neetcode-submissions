class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        answer = []
        for num in nums: 
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        sorted_nums = sorted(count, key=count.get, reverse=True)

        print(sorted_nums)

        for i in range(k):
            answer.append(sorted_nums[i])
        
        return answer