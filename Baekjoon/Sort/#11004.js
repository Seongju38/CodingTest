// https://www.acmicpc.net/problem/11004

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [N, K] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);

arr.sort(function (a, b) {
  return a - b;
});

console.log(arr[K - 1]);
