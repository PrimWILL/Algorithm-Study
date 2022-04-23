class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        
        for string in strs:
            anagram[''.join(sorted(string))].append(string)
        
        return list(anagram.values())