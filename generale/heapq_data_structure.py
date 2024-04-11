import heapq


h = []

heapq.heappush(h, -5)
heapq.heappush(h, -2)
heapq.heappush(h, -9)
heapq.heappush(h, 1)

print(h)

heapq.heappop(h)
print(h)
heapq.heappop(h)
print(h)
