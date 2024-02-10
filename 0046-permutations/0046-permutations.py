class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve_permutation(liste):
            result=[]
            if len(liste)==1:
                return [liste[:]]


            for i in range(len(liste)):

                n=liste.pop(0)


                perms=(solve_permutation(liste))

                for perm in perms:
                    perm.append(n)
                result.extend(perms)
                liste.append(n)
            return result
        return solve_permutation(nums)