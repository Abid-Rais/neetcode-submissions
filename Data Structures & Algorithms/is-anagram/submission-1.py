class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharCount = {}
        tCharCount = {}
        
        for char in s:
            sCharCount[char] = sCharCount.get(char, 0) + 1
        
        for char in t:
            tCharCount[char] = tCharCount.get(char, 0) + 1

        if len(sCharCount) != len(tCharCount): 
            return False
        
        for char, count in sCharCount.items():  
            if count != tCharCount.get(char, 0): 
                return False

        return True