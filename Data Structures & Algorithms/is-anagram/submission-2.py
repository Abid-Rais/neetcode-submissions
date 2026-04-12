class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sChar = s[i]
            sMap[sChar] = sMap.get(sChar, 0) + 1

            tChar = t[i]
            tMap[tChar] = tMap.get(tChar, 0) + 1

        return sMap == tMap
        
