class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d ={}
        if len(s) != len(t):
            return False
        for i in s :
            d[i] = d.get(i,0)+1
        for i in t:
            if (i in d.keys()) and d[i]:
                d[i]-=1
            else:
                return False
        return True
        
        