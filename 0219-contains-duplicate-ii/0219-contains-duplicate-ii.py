class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsdict=dict()
        for j,i in enumerate(nums):
            if i not in numsdict:
                numsdict[i]=[j]
            else:
                if j-numsdict[i][-1]<=k:
                    return True
                numsdict[i].append(j)
        return False