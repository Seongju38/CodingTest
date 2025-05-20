// https://www.acmicpc.net/problem/10974

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let N = Number(input[0]);
let arr = [];
for (let i = 1; i <= N; i++) arr.push(i);
let visited = new Array(N).fill(false);
let selectedIdx = [];

let answer = "";
function backtrack(arr, depth) {
  if (depth === N) {
    let resultArr = [];
    for (let s of selectedIdx) resultArr.push(arr[s]);
    for (let r of resultArr) answer += r + " ";
    answer += "\n";
    return;
  }
  for (let i = 0; i < N; i++) {
    if (!visited[i]) {
      selectedIdx.push(i);
      visited[i] = true;
      backtrack(arr, depth + 1);
      selectedIdx.pop();
      visited[i] = false;
    }
  }
}
backtrack(arr, 0);
console.log(answer);
