class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for n in nums:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
        
        s = sorted(d.items(), key=lambda count: count[1], reverse=True)
        res=[]
        for i in range(k):
            res.append(s[i][0])
        return res