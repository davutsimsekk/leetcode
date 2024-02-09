class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2 = []
        i = 0
        while i != len(arr)-1:

            maxi = max(arr[i+1:])

            arr2.append(maxi)
            i += 1
            while maxi > arr[i]:
                arr2.append(maxi)
                i += 1

        arr2.append(-1)
        return arr2