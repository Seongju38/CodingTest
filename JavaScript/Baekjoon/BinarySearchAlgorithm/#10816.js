// https://www.acmicpc.net/problem/10816

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let haveCardArr = input[1].split(" ").map(Number);
haveCardArr.sort((a, b) => a - b);
let checkCardArr = input[3].split(" ").map(Number);

let result = "";

for (let check of checkCardArr) {
  result += countByRange(haveCardArr, check, check) + " ";
}
console.log(result);

function lowerBound(arr, target, start, end) {
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (arr[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return end;
}

function upperBound(arr, target, start, end) {
  while (start < end) {
    let mid = parseInt((start + end) / 2);
    if (arr[mid] > target) end = mid;
    else start = mid + 1;
  }
  return end;
}

function countByRange(arr, leftValue, rightValue) {
  let rightIndex = upperBound(arr, rightValue, 0, arr.length);
  let leftIndex = lowerBound(arr, leftValue, 0, arr.length);
  return rightIndex - leftIndex;
}
