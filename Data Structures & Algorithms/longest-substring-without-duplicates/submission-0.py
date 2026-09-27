class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        check = set()
        length = 0

        while right < len(s):
            while s[right] in check:
                check.remove(s[left])
                left += 1

            check.add(s[right])
            length = max(length, right - left + 1)

            right += 1

        return length

