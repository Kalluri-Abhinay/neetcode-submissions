class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for i in s:
            f[i] = f.get(i,0)+1
        for k,v in f.items():
            if v==1:
                return s.index(k)
        return -1