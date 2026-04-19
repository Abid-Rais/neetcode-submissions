class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Ptr, word2Ptr = 0, 0
        res = ""
        while word1Ptr < len(word1) and word2Ptr < len(word2): 
            res += word1[word1Ptr] + word2[word2Ptr]
            word1Ptr += 1
            word2Ptr += 1

        if word1Ptr < len(word1): 
            res += word1[word1Ptr:]
        
        if word2Ptr < len(word2): 
            res += word2[word2Ptr:]

        return res
