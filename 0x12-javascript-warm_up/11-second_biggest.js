#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const numArgs = args.length;

if (numArgs === 0 || numArgs === 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  const secondLargest = sortedArgs[1];
  console.log(secondLargest);
}
