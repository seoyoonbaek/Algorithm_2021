import heapq
import sys
read = sys.stdin.readline

n = int(read())
h = []

for i in map(int, read().split()):
        heapq.heappush(h, i)

for _ in range(1, n):
    for i in map(int, read().split()):
        heapq.heappush(h, i)
        heapq.heappop(h)

print(h[0])

#n번째 큰 수 -> heapq길이 n 유지!! 
