'''
음료수 얼려 먹기

N x M 크기의 얼음 틀
구멍이 뚫려 있는 부분 : 0, 칸막이가 존재하는 부분 : 1
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주

입력조건 ) 첫째 줄에 얼음 틀의 세로 길이 N 과 가로 길이 M 이 주어짐 (1 <= N, M <= 1,000)
둘째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어짐

출력조건 ) 한 번에 만들 수 있는 아이스크림의 개수 출력

[입력]                      [출력]
15 14                       8
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

import sys
sys.stdin = open('input.txt', 'r')

# 공백으로 구분된 N, M 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 해당 노드 방문 처리
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)