#!/usr/bin/node
const x = process.argv.length;
if (x === 2 || x === 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i <= x - 1; i++) {
    arr.unshift(process.argv[i]);
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
