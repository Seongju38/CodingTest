// 이진 탐색 소스 구현 (반복문)
function binarySearch(arr, target, start, end) {
  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    if (arr[mid] == target) return mid;
    else if (arr[mid] > target) end = mid - 1;
    else start = mid + 1;
  }
  return -1;
}

// 사용 예시
let n = 10;
let target = 7;
let arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
let result = binarySearch(arr, target, 0, n - 1);
if (result == -1) console.log("원소가 존재하지 않습니다.");
else console.log(`${result + 1}번째 원소입니다.`);
