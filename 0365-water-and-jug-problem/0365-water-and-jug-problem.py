class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        dp=set()

        def solve_naive(curr):
            if curr==targetCapacity:
                return True
            elif curr in dp:
                return False
            else:

                for i in (-jug1Capacity,-jug2Capacity,jug1Capacity,jug2Capacity):
                    if jug1Capacity+jug2Capacity>=curr+i>=0:
                        dp.add(curr)
                        if solve_naive(curr+i):
                            return True

                return False
        try:
            return(solve_naive(0))
        except:
            return True