#!/usr/bin/node
const arg = process.argv[2];
const x = parseInt(arg);

if (!isNaN(x)) {
  let output = "";
  for (let i = 0; i < x; i++) {
    output += "C is fun\n";
  }
  console.log(output.trim());
} else {
  console.log("Missing number of occurrences");
}
