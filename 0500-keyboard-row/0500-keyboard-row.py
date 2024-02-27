class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstrow=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        secondrow=['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        thirdrow=['z', 'x', 'c', 'v', 'b', 'n', 'm']
        result=[]
        counter=0
        for word in words:
            addornot=True
            word=word.lower()
            ilkharf=word[0]
            if ilkharf in firstrow:
                for letter in word[1:]:
                    if letter not in firstrow:
                        addornot=False
                        break
                if addornot==True:
                    result.append(words[counter])
            elif ilkharf in secondrow:
                for letter in word[1:]:
                    if letter not in secondrow:
                        addornot=False
                        break
                if addornot==True:
                    result.append(words[counter])
            elif ilkharf in thirdrow:
                for letter in word[1:]:
                    if letter not in thirdrow:
                        addornot=False
                        break
                if addornot==True:
                    result.append(words[counter])
            counter+=1
        return(result)