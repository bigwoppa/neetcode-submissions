class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            count = [0 for _ in range(26)]
            

            for l in s:
                count[ord(l) - ord("z")] += 1
                
            result[tuple(count)].append(s)
        return list(result.values())

        result = defaultdict(list)