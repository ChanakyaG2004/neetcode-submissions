class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        start = strs[0]

        for word in strs:
            while not word.startswith(start):
                start = start[:-1]

                if start == "":
                    return ""

        return start
