from collections import deque
import sys
read = sys.stdin.readline

def bfs(v, cnt):
    q = deque([[v, cnt]])
    visited[v] = True

    while q:
        v, cnt = q.popleft()
        #버튼 횟수니까 첫 시작 층에서는 cnt 없는 게 맞
        #cnt+=1

        #(uv or du)==G말고 이게 맞음(queue는 다음 갈 곳들을 넣어두는 것 뿐, 진짜 움직이는 건 pop할 때니까!)
        if v==G:
            return cnt
        
        uv = v + U
        dv = v - D

        if 0<uv<=F and visited[uv]==False:
            q.append([uv, cnt+1])
            visited[uv]==True

        if 0<dv<=F and visited[dv]==False:
            q.append([dv, cnt+1])
            visited[dv]==True
    
    return "use the stairs"


F, S, G, U, D = map(int, read().split())    #s->g

#빈list -> in 사용해도 됨
visited = [False]*(F+1)

print(bfs(S, 0)) 





#최솟값 = bfs
#https://jjangsungwon.tistory.com/35
