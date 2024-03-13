class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap=[]
        if ladders==0:
            for i in range(len(heights)-1):
                
                fark=heights[i+1]-heights[i]
                if fark<=0:
                    continue
                    
                if bricks<fark:
                    return i
                else:
                    bricks-=fark
            return len(heights)-1

        for i in range(len(heights)-1):
            fark=heights[i+1]-heights[i]
            if heights[i]>=heights[i+1]:
                continue
            elif ladders>0:
                ladders-=1
                heapq.heappush(minheap,fark)
            else:
                mini=minheap[0]
                if mini<fark:
                    if heapq.heappop(minheap)<=bricks:  
                        heapq.heappush(minheap,fark)
                        bricks-=mini
                    else:
                        return i
                else:
                    if fark>bricks:
                        return i
                    else:
                        bricks-=fark
        return len(heights)-1