array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, startIdx, endIdx):
    if startIdx >= endIdx: # 원소가 1개인 경우 종료
        return
    
    pivotIdx = startIdx # 피벗은 첫 번째 원소
    leftIdx = startIdx + 1
    rightIdx = endIdx

    while leftIdx <= rightIdx:
        # 피벗보다 큰 데이터를 찾을 떄까지 반복
        while leftIdx <= endIdx and array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while rightIdx > startIdx and array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
        
        if leftIdx > rightIdx: # 엇갈렸다면 작은 데이터와 피벗 교체
            array[rightIdx], array[pivotIdx] = array[pivotIdx], array[rightIdx]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, startIdx, rightIdx - 1)
    quick_sort(array, rightIdx + 1, endIdx)

quick_sort(array, 0, len(array) - 1)

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]