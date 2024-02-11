class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        textlist=text.split()
        result=0
        for i in textlist:
            result+=1
            for j in i:
                if j in brokenLetters:
                    result-=1
                    break
        return result