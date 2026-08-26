class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checkOne = {}
        checkTwo = {}

        right = 0
        left = 0

        for char in s1:
            if char in checkOne:
                checkOne[char] += 1
            else:
                checkOne[char] = 1
        
        while right < len(s2):
            if s2[right] in checkTwo:
                checkTwo[s2[right]] += 1
            else:
                checkTwo[s2[right]] = 1
            
            while right - left + 1 > len(s1):
                checkTwo[s2[left]] -= 1
                if checkTwo[s2[left]] == 0:
                    del checkTwo[s2[left]]
                left += 1
            
            if checkOne == checkTwo:
                return True
            
            right += 1
        

        return False




