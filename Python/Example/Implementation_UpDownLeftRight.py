'''
상하좌우

A는 N x N 크기의 정사각형 공간 위에 서 있고 이 공간은 1 x 1 크기의 정사각형으로 나누어져있음
가장 왼쪽 위 좌표는 (1, 1) 이고 가장 오른쪽 아래 좌표는 (N, N) 에 해당함
A는 상, 하, 좌, 우 방향으로 이동할 수 있으며 시작 좌표는 항상 (1, 1)
이동 계획서는 하나의 줄에 띄어쓰기를 기준으로
    L : 왼쪽으로 한 칸 이동
    R : 오른쪽으로 한 칸 이동
    U : 위로 한 칸 이동
    D : 아래로 한 칸 이동
중 하나의 문자가 반복적으로 적혀있음
이 때 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됨

입력조건 ) 첫째 줄에 공간의 크기를 나타내는 N (1 <= N <= 100) 이 주어지고
둘쨰 줄에 A가 이동할 계획서 내용 (1 <= 이동 횟수 <= 100) 이 주어짐

출력조건 ) 첫째 줄에 A가 최종적으로 도착할 지점의 좌표 (X, Y) 를 공백으로 구분하여 출력

[입력]                      [출력]
5                           3 4
R R R U D D
'''

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
plans = input().split()

directions = {
    'L' : [0, -1],
    'R' : [0, 1],
    'U' : [-1, 0],
    'D' : [1, 0]
}

x, y = [1, 1]
for plan in plans:
    
    ## 중복 계산 줄이기 ##
    dx, dy = directions[plan]
    nx, ny = x + dx, y + dy
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny


    # checkX = x + directions[plan][0]
    # checkY = y + directions[plan][1]
    
    # if checkX > 0 and checkY > 0 and checkX <= n and checkY <= n:
    #     x = x + directions[plan][0]
    #     y = y + directions[plan][1]

print(x, y)
