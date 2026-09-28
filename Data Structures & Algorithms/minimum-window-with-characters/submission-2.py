class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        checkt = {}
        checks = {}

        for char in t:
            if char in checkt:
                checkt[char] += 1
            else:
                checkt[char] = 1

        need = len(checkt)
        have = 0

        left = 0
        answer = ""
        min_length = float("inf")

        for right in range(len(s)):
            char = s[right]

            if char in checkt:
                if char in checks:
                    checks[char] += 1
                else:
                    checks[char] = 1

                if checks[char] == checkt[char]:
                    have += 1

            while have == need:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    answer = s[left:right + 1]

                left_char = s[left]

                if left_char in checkt:
                    if checks[left_char] == checkt[left_char]:
                        have -= 1

                    checks[left_char] -= 1

                left += 1

        return answer