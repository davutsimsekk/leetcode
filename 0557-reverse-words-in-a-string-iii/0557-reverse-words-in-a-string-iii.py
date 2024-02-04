class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        liste = s.split()
        resultlist=[]
        for i in range(len(liste)):
            if i!=0:
                resultlist.append(" ")
            for j in range(len(liste[i]) - 1, -1, -1):
                resultlist.append(liste[i][j])
        result="".join(resultlist)
        return(result)