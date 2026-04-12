class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestWord = strs[0]
        for word in strs: 
            if len(word) < len(shortestWord): 
                shortestWord = word

        prefix = ""
        for i in range(len(shortestWord)):
            for word in strs: 
                if shortestWord[i] != word[i]: 
                    return prefix

            prefix += shortestWord[i]

        return prefix