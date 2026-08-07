class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for s in strs:
            c = str(sorted(s))
            if c in d.keys():
                d[c].append(s)
            else:
                d[c] = [s]
        
        return list(d.values())