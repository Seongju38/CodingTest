// 병합 수행 함수
function merge(arr, sorted, left, mid, right) {
  let i = left;
  let j = mid + 1;
  let k = left;

  while (i <= mid && j <= right) {
    // 오름차순
    if (arr[i] <= arr[j]) sorted[k++] = arr[i++];
    else sorted[k++] = arr[j++];
  }

  if (i > mid) {
    for (; j <= right; j++) sorted[k++] = arr[j];
  } else {
    for (; i <= mid; i++) sorted[k++] = arr[i];
  }

  for (let x = left; x <= right; x++) {
    arr[x] = sorted[x];
  }
}

// 병합 정렬 함수
function mergeSort(arr, sorted, left, right) {
  if (left < right) {
    let mid = parseInt((left + right) / 2);

    mergeSort(arr, sorted, left, mid);
    mergeSort(arr, sorted, mid + 1, right);
    merge(arr, sorted, left, mid, right);
  }
}

// 사용 예시
const arr = [12, 11, 13, 5, 6, 7];
const sorted = new Array(arr.length);
mergeSort(arr, sorted, 0, arr.length - 1);
console.log(arr);
