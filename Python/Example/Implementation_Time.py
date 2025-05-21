'''
시각

정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성
예를 들어 1을 입력했을 때
    00시 00분 03초
    00시 13분 30초
는 3이 하나라도 포함되어 있으므로 세어야 하는 시각
반면
    00시 02분 55초
    01시 27분 45초
는 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각

입력조건 ) 첫째 줄에 정수 N (0 <= N <= 23) 입력

출력조건 ) 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력

[입력]                      [출력]
5                           11475
'''

import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

count = 0
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)