import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph
        graph = {i: [] for i in range(n)}
        for from_, to, cost in flights:
            graph[from_].append((to, cost))

        # Perform Dijkstra's
        shortest = {n: (float('inf'), float('inf')) for n in graph.keys()}
        edgeQueue = [(0, 0, src)]
        while len(edgeQueue):
            totalCost, totalStops, node = heapq.heappop(edgeQueue)

            if node == dst:
                return totalCost
            if totalStops > k or totalStops > shortest[node][1]:
                continue

            shortest[node] = (totalCost, totalStops)

            for neighbor, cost in graph[node]:
                tentativeCost = totalCost+cost
                tentativeStops = totalStops+1
                heapq.heappush(edgeQueue, (tentativeCost, tentativeStops, neighbor))

        return -1
