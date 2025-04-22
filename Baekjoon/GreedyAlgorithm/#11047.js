// https://www.acmicpc.net/problem/11047

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0].split(" ")[0]);
let K = Number(input[0].split(" ")[1]);

let coins = [];
for (let i = 1; i <= N; i++) {
  coins[N - i] = Number(input[i]);
}

let cnt = 0;
for (let i = 0; i < N; i++) {
  if (coins[i] <= K) {
    cnt += parseInt(K / coins[i]);
    K = K - coins[i] * parseInt(K / coins[i]);
  }
}

console.log(cnt);
