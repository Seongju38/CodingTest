// https://www.acmicpc.net/problem/1654

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let K = Number(input[0].split(" ")[0]);
let N = Number(input[0].split(" ")[1]);
let arr = [];
for (let i = 1; i <= K; i++) {
  arr.push(Number(input[i]));
}

let start = 1;
let end = Math.max(...arr);

let result = 0;
while (start <= end) {
  let mid = parseInt((start + end) / 2);

  let cnt = 0;
  for (let len of arr) {
    cnt += parseInt(len / mid);
  }

  if (cnt < N) {
    end = mid - 1;
  } else {
    result = mid;
    start = mid + 1;
  }
}
console.log(result);
