
from queue import Queue

def bfs_cc(adj, vtx, color, s, visited): # 연결된 그래프끼리 묶어주는 함수
    q = Queue() # 큐 생성
    q.put(s) # s 큐에 대입
    visited.add(s) # s 방문
    color.append(s) # s 방문 했으므로 color로 묶음
    while q.qsize() != 0: # 큐가 공백이 될 때까지
        v = q.get() # 큐에서 정점 빼고 반환
        for idx, node in enumerate(adj[vtx.index(v)]): # v에서의 adj의 인덱스 및 정점여부 반환
            if node and vtx[idx] not in visited: # 정점여부 판별 그리고 방문여부 판별하여
                visited.add(vtx[idx]) # visited에 해당 정점 추가
                q.put(vtx[idx]) # 큐에 해당 정점 추가
                if vtx[idx] not in color: # 해당 정점 color에서의 유뮤 여부 판별
                    color.append(vtx[idx]) # color에 정점 추가
    return color # color 반환

def find_connected_component(adj, vtx): # 같은 color끼리 묶는 함수
    visited = set() # 이미 방문한 정점의 집합
    colorList = [] # 부분 그래프별 정점 리스트

    for s in vtx: # 하나의 정점에 대해
        if s not in visited: # 방문하지 않은 정점이라면
            color = bfs_cc(adj, vtx, [], s, visited) # 새로운 컬러 리스트
            colorList.append(color) # 컬러 리스트 추가

    return colorList

def find_bridges(adj, vtx): # 브릿지 탐색 함수
    bridges = list() # 브릿지 리스트
    marker = [] # 방문한 인덱스 저장 리스트
    for i in range(len(adj)):
        for j in range(len(adj)):
            if adj[i][j] == 1: # 해당 위치에 있는 정점과 연결되어 있다면
                adj[i][j] = 0 # 간선을 끊음
                adj[j][i] = 0 
                if len(find_connected_component(adj, vtx)) > 1 and (i, j) not in marker: # 결과의 그래프가 2개 나오고 marker에 표시되지 않았다면
                    bridges.append((vtx[i], vtx[j])) # 브릿지 리스트에 해당 간선의 정점 추가
                    marker.append((i, j)) # 방문한 인덱스를 저장
                    marker.append((j, i))
                adj[i][j] = 1 # 재 테스트를 위해 간선 재연결
                adj[j][i] = 1
    return bridges


vertex =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 정점 리스트
adjMat =  [ [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0] ] # 간선 리스트

print('find_bridges: ')
print(find_bridges(adjMat, vertex)) # 브릿지 탐색 함수 실행
print()
print(find_connected_component(adjMat, vertex))