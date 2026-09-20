class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        answer = []
        current = intervals[0]
        for interval in intervals[1::]:
            if current[0] <= interval[1] and current[1] >= interval[0]:
                current = [current[0], max(current[1], interval[1])]
            else:
                answer.append(current)
                current = interval
        
        answer.append(current)
        return answer

            
