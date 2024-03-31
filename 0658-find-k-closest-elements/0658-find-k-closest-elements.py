class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
   

        if len(arr)<k:
            return []


        l=0
        r=len(arr)-1
        mid=(r+l)//2
        while l!=r:
            mid=(l+r)//2
          
            if (r-l==1):
                if x==arr[l]:
                    mid=l
                    break
                elif x==arr[r]:
                    mid=r
                    break
                
                
                if x<arr[l]:
                    mid=l
                    break
                elif x>arr[r]:
                    mid=r+1
                    break
                elif arr[l]<x<arr[r]:
                    mid=r
                    break

            
            if arr[mid]>x:
                r=mid
            elif arr[mid]<x:
                l=mid
            elif arr[mid]==x:
                
                break



        res=[]
        leftp=mid-1
        rigthp=mid
        while k!=0:

            
            if leftp<0 and rigthp>=len(arr):
                break
            
            elif rigthp>=len(arr):
                res.append(arr[leftp])
                leftp-=1
                
            elif leftp<0:
                
                res.append(arr[rigthp])
                rigthp+=1
            
            
                
            else:
                if abs(arr[rigthp]-x)<abs(arr[leftp]-x):
                    
                    res.append(arr[rigthp])
                    rigthp+=1
                    
                else:
                    
                    res.append(arr[leftp])
                    
                    leftp-=1
                    
            k-=1
    
        return(sorted(res))