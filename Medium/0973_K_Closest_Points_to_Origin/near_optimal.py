import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Customize input (O(n), O(n))
        pointsCustom = [CustomPoint(point) for point in points]

        # Heapify (O(n))
        heapq.heapify(pointsCustom)

        # Pop (O(klog(n)))
        result = []
        for i in range(k):
            value = heappop(pointsCustom)
            result.append([value.coordinates[0], value.coordinates[1]])

        # O(n + klog(n))
        return result

class CustomPoint:
    def __init__(self, point):
        self.coordinates = (point[0], point[1])
        self.magnitude = vector_magnitude(self.coordinates)

    def __lt__(self, other):
        return self.magnitude < other.magnitude

def vector_magnitude(p):
    x, y = p[0], p[1]
    return ((x**2)+(y**2))**(1/2)