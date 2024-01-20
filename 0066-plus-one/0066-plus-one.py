class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=""
        result=[]
        for i in digits:
            string+=str(i)
        string=str(int(string)+1)
        for i in string:
            result.append(int(i))

        return(result)
