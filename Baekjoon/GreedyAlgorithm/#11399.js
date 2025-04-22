// https://www.acmicpc.net/problem/11399

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let times = input[1].split(" ").map(Number);

times.sort((a, b) => a - b);

let total = 0;
for (let i = 0; i < N; i++) {
  total += times[i] * (N - i);
}

console.log(total);
