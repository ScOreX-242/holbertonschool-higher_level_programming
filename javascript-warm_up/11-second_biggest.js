#!/usr/bin/node
const args = process.argv.slice(2).map((value) => parseInt(value, 10));

if (args.length < 2) {
  console.log(0);
} else {
  const uniqueValues = [...new Set(args)].sort((left, right) => right - left);
  console.log(uniqueValues.length > 1 ? uniqueValues[1] : 0);
}
