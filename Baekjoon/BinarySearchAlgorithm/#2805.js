// https://www.acmicpc.net/problem/2805

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let treeLength = Number(input[0].split(" ")[1]);
let treeHeightArr = input[1].split(" ").map(Number);
let result = 0;

let start = 1;
let end = Math.max(...treeHeightArr);

while (start <= end) {
  let mid = parseInt((start + end) / 2);

  let sum = 0;
  for (let height of treeHeightArr) {
    height -= mid;
    if (height > 0) sum += height;
  }

  if (sum >= treeLength) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);
