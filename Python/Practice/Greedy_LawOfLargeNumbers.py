'''
큰 수의 법칙

다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없고
서로 다른 인덱스가 해당하는 수가 같은 경우에도 서로 다른 것으로 간주

입력조건 ) 첫째 줄에 배열의 크기 N (2 <= N <= 1,000), 숫자가 더해지는 횟수 M (1 <= M <= 10,000), K (1 <= K <= 10,000) 의 자연수가 공백으로 구분되어 주어지고
둘째 줄에 N개의 자연수 (각각의 자연수는 1 이상 10,000 이하의 수) 가 공백으로 구분되어 주어지고
입력으로 주어지는 K는 항상 M보다 작거나 같음

출력조건 ) 첫째 줄에 큰 수의 법칙에 따라 더해진 답 출력

[입력]                      [출력]
5 8 3                       46
2 4 5 4 6
'''

### 반복되는 수열에 대해서 파악 ###

import sys
sys.stdin = open('input.txt', 'r')

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
firstBig = arr[n - 1]
secondBig = arr[n - 2]

firstBigCount = m // (k + 1) * k + m % (k + 1)
secondBigCount = m - firstBigCount

print(firstBig * firstBigCount + secondBig * secondBigCount)