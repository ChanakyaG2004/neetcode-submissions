class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        currOutput = []
        output = []
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        for key in groups:
            output.append(groups[key])
        
        return output
        
            

            
            
        