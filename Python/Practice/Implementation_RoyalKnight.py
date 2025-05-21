'''
왕실의 나이트

왕실 정원은 8 x 8 좌표 평면 (행 위치 1부터 8 로 표현, 열 위치 a부터 h로 표현)
나이트는 이동 할 때 L자 형태로만 이동 가능하며 정원 밖으로는 나갈 수 없음
또한, 특정한 위치에서
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
이 경우로 이동 가능

입력조건 ) 첫째 줄에 8 x 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열 입력
a1 처럼 열과 행으로 이뤄짐

출력조건 ) 첫째 줄에 나이트가 이동할 수 있는 경우의 수 출력

[입력]                      [출력]
a1                          2
'''

import sys
sys.stdin = open('input.txt', 'r')

input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1 # 'a' 는 97, 1부터 시작하게끔 + 1
# column = ord(input_data[0]) - 96

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [
    (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2) 
]

count = 0
for step in steps:

    ## 이동 기준 좌표를 변경해서 오류 발생 ##
    # row, column = row + step[0], column + step[1]
    
    # if 0 < row <= 8 and 0 < column <= 8:
    #     count += 1

    next_row, next_col = row + step[0], column + step[1]

    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1
        
print(count)
