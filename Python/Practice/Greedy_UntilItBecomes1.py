'''
1이 될 때까지

주어진 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
    1. N에서 1 뺴기
    2. N을 K로 나누기 (N이 K로 나누어떨어질 때만 선택 가능)

입력조건 ) 첫째 줄에 N (2 <= N <= 100,000)과 K (2 <= K <= 100,000)가 공백으로 구분되며 각각 자연수로 주어지고
이때 입력으로 주어지는 N은 항상 K보다 크거나 같음

출력조건 ) 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값 출력

[입력]                      [출력]
25 5                        2
'''

### 최대한 많이 나누기 ###

import sys
sys.stdin = open('input.txt', 'r')

## 25 → 5 (한 번에 20 빼고) → 1 (한 번 나누기) ##
result = 0
while n >= k:
    # (N == K로 나누어떨어지는 수)가 될 때까지 한 번에 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # K로 나누기
    n //= k
    result += 1

# 마지막 남은 수에 대하여 1씩 뺴기
result += (n - 1)

print(result)


## 25 → 24 → 23 → ... → 5 → 1 (많은 연산 필요) ##
# n, k = map(int, input().split())

# count = 0
# while True:
#     if n == 1:
#         break

#     if n % k == 0:
#         n //= k
#         count += 1
#     else:
#         n -= 1
#         count += 1

# print(count)