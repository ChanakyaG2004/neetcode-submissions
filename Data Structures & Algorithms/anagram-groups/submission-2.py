class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        check = {}

        for word in strs: 
            key = "".join(sorted(word))
            if key in check:
                check[key].append(word)
            else:
                check[key] = [word]

        return list(check.values())