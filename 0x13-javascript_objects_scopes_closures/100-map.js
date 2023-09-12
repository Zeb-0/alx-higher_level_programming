#!/usr/bin/node
const list = require('./100-data.js').list; // Import the array from 100-data.js

// Use the map method to create a new array based on the original list
const newList = list.map((value, index) => value * index);

// Print both the initial and new arrays
console.log(list);
console.log(newList);

