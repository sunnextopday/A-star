import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def solve(Graph, Start):
    prev = [-1] * (len(Graph))
    dist = [INF] * (len(Graph))
    dist[Start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, Start])

    while priority_queue:
        # 거리가 제일 작은 노드 선택
        current_dist, here = heapq.heappop(priority_queue)

        # 인접 노드 iteration
        for there, length in Graph[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])

    return dist, prev

if __name__ == "__main__":
    V, E = map(int, input().split())
    Start = int(input())
    Graph = [{} for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())

        # 만약 동일한 경로의 간선이 주어질 경우 적은 비용의 간선 선택
        if v in Graph[u]:
            Graph[u][v] = min(Graph[u][v], w)
        else:
            Graph[u][v] = w

    dist, prev = solve(Graph, Start)

    for i in dist[1:]:
        print(i if i != INF else "INF")