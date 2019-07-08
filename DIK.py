import sys

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(Start, CN, Graph):
    visit = [False] * CN # 특정 노드를 방문했는지 알기 위한 체킹 배열 노드 수 만큼 크기 지정 및 False로 초기화
    dist = [INF] * CN # 한 노드 마다의 최소 간선 값을 저장 하기 위한 배열 노드 수 만큼 크기 지정 및 INF 값으로 초기화

    dist[Start - 1] = 0 # 시작 노드 dist 값은 0으로 초기화

    while True:
        min = INF
        N = -1

        for j in range(CN):
            if not visit[j] and min > dist[j]: # 방문한 적이 없고 min보다 dist 값이 크면 min값 과 N값을 교체해 체인지을 시도한다
                min = dist[j]
                N = j

        if min == INF: # 노드들을 방문한게 없으면 반복문을 나간다
            break

        visit[N] = True # if문을 안타면 최단 간선 값을 가진 노드를 방문했다고 체크

        for j in range(CN):
            if visit[j]: continue # 방문한 적이 있으면 skip
            via = dist[N] + Graph[N][j] # 없으면 dist N값 과 그래프 간선 값을 더하여
            if dist[j] > via: # dist의 j가 합계 값 보다 크면 dist의 j번지에 값을 바꾼다
                dist[j] = via

    return dist

if __name__ == "__main__":
    CN, CW = map(int, input().split()) #노드 수 , 간선 수 지정
    Start = int(input()) # 탐색에 시작이 되는 노드 설정
    Graph = [[INF] * CN for _ in range(CN)] #그래프 2차원 배열 노드 수 만큼 크기를 지정 및 INF 값으로 초기화

    for _ in range(CW): # 간선 수 만큼 그래프에 간선 값 대입
        u, v, w = map(int, input().split())
        Graph[u - 1][v - 1] = w

    for i in dijkstra(Start, CN, Graph):
        print(i if i != INF else "INF")