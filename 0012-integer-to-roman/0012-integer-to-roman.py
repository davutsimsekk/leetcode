class Solution:
    def intToRoman(self, num: int) -> str:
        r_dict={
        "I":1,
        "IV":4,       
        "V":5,
        "IX":9,
        "X":10,
        "XL": 40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000
        }

        result=""
        while num!=0:
            for i,j in enumerate(reversed(list(r_dict.values()))):
                if num>=j:
                    result+=list(r_dict.keys())[-i-1]
                    num-=j
                    break
        return(result)