class Solution:
    def countPrimes(self, n: int) -> int:
        if n==2:
            return 0
        res=0
        arr=[]
        for i in range(n):
            if i%2==1:
                res+=1
                arr.append(True)
            else:
                arr.append(False)

        for i in range(3,int(n**0.5)+1):
            if arr[i]==True:
                for j in range(3,int(i**0.5)+1):
                    if i%j==0:
                        arr[i-2]=False
                        break
                if arr[i]==True:
                    j=2
                    while j*i<n:
                        if arr[i*j]!=False:
                            res-=1
                            arr[i*j]=False
                        
                        
                        j+=1
        
        return(res)