#https://leetcode.com/problems/network-delay-time

import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u,v,w in times:
            graph[u].append((v,w))
            
        # made graph
        
        pq = [(0,k)]
        dist = {}
        
        while pq:
            
            d,node = heapq.heappop(pq)
            
            if node in dist: continue
            
            dist[node] = d
            
            for n ,d2 in graph[node]:
                if n not in dist:
                    heapq.heappush(pq,(d+d2,n))
        
        
