class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2,t2=set(s),set(t)
        
        if len(s) != len(t):
            return False

        for i in s2:
            if i not in t2 or s.count(i) !=t.count(i):
                return False
        else:
            return True
        