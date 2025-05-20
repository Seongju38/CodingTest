// https://www.acmicpc.net/problem/18870

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let set = new Set(arr);
let arrForSort = [...set];
arrForSort.sort(function (a, b) {
  return a - b;
});

let valueForMatch = {};
for (let i = 0; i < arrForSort.length; i++) {
  valueForMatch[arrForSort[i]] = i;
}

let result = "";
for (let i = 0; i < N; i++) {
  if (valueForMatch.hasOwnProperty(arr[i])) {
    result += valueForMatch[arr[i]] + " ";
  }
}

console.log(result);
