class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = {}
        left = 0
        right = 0
        length = 0

        while right < len(s):
            if s[right] in check:
                check[s[right]] += 1
            else:
                check[s[right]] = 1
            
            maxFreq = max(check.values())

            while (right - left + 1) - maxFreq > k:
                check[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
        
            right += 1
        
        return length



            
        