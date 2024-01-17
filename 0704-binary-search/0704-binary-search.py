class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indexi=0
        def solve_binary(liste,target):
            nonlocal indexi
            if len(liste)==1 and liste[0]!=target:
                return -1
            if target>liste[len(liste)//2]:
                indexi+=len(liste)//2
                return solve_binary(liste[len(liste)//2:],target)
            elif target<liste[len(liste)//2]:
                return solve_binary(liste[:len(liste)//2],target)
            else:
                return (indexi+(len(liste)//2))


        return(solve_binary(nums,target))