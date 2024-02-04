class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_one=0
        index_two=len(numbers)-1

        while index_one<index_two:
            tmp=numbers[index_one]+numbers[index_two]
            if tmp==target:
                return [index_one+1,index_two+1]
            elif tmp<target:
                index_one+=1
                continue
            elif tmp>target:
                index_two-=1