class Solution:
    def isPalindrome(self, x: int) -> bool:
        boolen=False
        x=str(x)
        y=str(x)
        y=y[::-1]
        if x==y:
            boolen=True
        return boolen    