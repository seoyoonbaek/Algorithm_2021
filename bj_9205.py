def check_graph():
    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue
            if abs(g_list[i][0]-g_list[j][0]) + abs(g_list[i][1]-g_list[j][1]) <= 1000:
                graph[i][j] = 1
                graph[j][i] = 1

def dfs(v):
    visited[v] = 1
    for i in range(n+2):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)
        
for _ in range(int(input())):
    n = int(input())
    g_list = [list(map(int, input().split())) for _ in range(n+2)]
    graph = [[0]*(n+2) for _ in range(n+2)]
    visited = [0]*(n+2)
    check_graph()
    dfs(0)
    print("happy" if visited[-1] else "sad")
