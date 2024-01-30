class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result=0
        for word in words:
            result+=1
            for letter in word:
                if letter not in allowed:
                    result-=1
                    break
                    
        return result