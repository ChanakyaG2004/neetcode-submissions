class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = {}
        for letter in magazine:
            if letter in magCount:
                magCount[letter] += 1
            else:
                magCount[letter] = 1
        
        for letter in ransomNote:
            if letter in magCount:
                magCount[letter] -= 1
                if magCount[letter] == 0:
                    del magCount[letter]
            else:
                return False
        
        return True