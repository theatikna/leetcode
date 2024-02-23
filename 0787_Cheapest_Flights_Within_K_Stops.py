class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        D = defaultdict(set)
        for s,d,p in flights:
            D[s].add((d,p))
        seen = defaultdict(lambda:-2) # how many stops we already used when visited a node
        heap = [(0, src, k)] # price, curnode, remaining stop count
        while heap:
            price, cur, k = heappop(heap)
            if cur == dst:
                return price
            if seen[cur] > k or k < 0: # 1:when visited cur earlier, did we have more remaining stops than now,  2: have we exhausted all the stops this time
                continue
            seen[cur] = k
            for d,p in D[cur]:
                heappush(heap, (price+p,d,k-1))
        return -1
