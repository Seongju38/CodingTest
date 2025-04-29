// https://www.acmicpc.net/problem/9009

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(input[0]);
for (let t = 1; t <= T; t++) {
  let n = Number(input[t]);
  let result = [];
  let fibonacciArr = fibonacci(n);
  fibonacciArr.sort((a, b) => b - a);

  result.push(fibonacciArr[0]);
  let remainValue = n - fibonacciArr[0];
  for (let i = 1; i < fibonacciArr.length; i++) {
    if (fibonacciArr[i] <= remainValue) {
      if (fibonacciArr[i] !== 0) result.push(fibonacciArr[i]);
      remainValue = remainValue - fibonacciArr[i];
    }
  }
  result.sort((a, b) => a - b);
  console.log(String(result).replaceAll(",", " "));
}

function fibonacci(n) {
  let max = 0;
  let i = 2;
  let arr = [];
  arr.push(0);
  arr.push(1);
  while (max < n) {
    if (n < arr[i - 1] + arr[i - 2]) break;
    arr[i] = arr[i - 1] + arr[i - 2];
    max = arr[i];
    i++;
  }
  return arr;
}
