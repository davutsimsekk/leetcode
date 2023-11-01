class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        liste = [0]*n
        for i in range(1,n+1):
            if not i%3 and not i%5:
                liste[i-1] = "FizzBuzz"
            elif not i%3:
                liste[i-1]="Fizz"
            elif not i%5:
                liste[i-1]="Buzz"
            else:
                liste[i-1]=str(i)
        return liste       
            
            
    