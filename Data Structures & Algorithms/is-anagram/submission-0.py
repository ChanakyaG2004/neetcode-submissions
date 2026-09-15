class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sCheck = {}
        tCheck = {}

        for char in s:
            if char in sCheck:
                sCheck[char] += 1
            else:
                sCheck[char] = 1
        
        for char in t:
            if char in tCheck:
                tCheck[char] += 1
            else:
                tCheck[char] = 1
        
        if sCheck == tCheck:
            return True
        else:
            return False
        
        return False