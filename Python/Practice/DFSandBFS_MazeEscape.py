'''
미로 탈출

N x M 크기의 직사각형 미로
현재 : (1, 1) , 미로의 출구 : (N, M) 위치에 존재
한 번에 한 칸씩 이동 가능
괴물이 있는 부분 : 0 , 괴물이 없는 부분 : 1 로 표시
미로는 반드시 탈출할 수 있는 형태로 제시

입력조건 ) 첫째 줄에 두 정수 N, M (4 <= N, M <= 200) 이 주어짐
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어지고
각각의 수들은 공백 없이 붙어서 입력으로 제시됨
시작 칸과 마지막 칸은 항상 1

출력조건 ) 첫쨰 줄에 최소 이동 칸의 개수 출력 (시작 칸과 마지막 칸 모두 포함해서 계산산)

[입력]                      [출력]
5 6                         18
101010
111111
000001
111111
111111
'''

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

# 공백으로 구분된 N, M 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))