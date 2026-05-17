#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  const numA = parseInt(a, 10);
  const numB = parseInt(b, 10);
  console.log(numA + numB);
}
add(a, b);
