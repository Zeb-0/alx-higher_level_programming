#!/usr/bin/node
const dict = require('./101-data.js').dict; // Import the dictionary from 101-data.js

// Create a new dictionary where keys are the 
// number of occurrences and values are lists of user ids
const occurrencesById = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrencesById[occurrences] === undefined) {
    occurrencesById[occurrences] = [];
  }
  occurrencesById[occurrences].push(userId);
}

// Print the new dictionary
console.log(occurrencesById);

