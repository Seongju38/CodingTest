// https://www.acmicpc.net/problem/2751

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);

let arr = [];
for (let i = 1; i <= N; i++) {
  arr.push(Number(input[i]));
}

arr.sort(function (a, b) {
  return a - b;
});

let result = "";
for (let i = 0; i < arr.length; i++) {
  result += arr[i] + "\n";
}

console.log(result);
