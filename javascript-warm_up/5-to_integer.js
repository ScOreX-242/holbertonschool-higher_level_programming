#!/usr/bin/node
const myVar = process.argv[2];
const num = parseInt(myVar, 10);
if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
