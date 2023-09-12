#!/usr/bin/node

const fs = require('fs');

// Ensure that the correct number of command line arguments are provided
if (process.argv.length !== 5) {
  console.log('Usage: node concat-files.js source1.txt source2.txt destination.txt');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

// Read the contents of the first source file
fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(`Error reading ${sourceFilePath1}: ${err1}`);
    process.exit(1);
  }

  // Read the contents of the second source file
  fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(`Error reading ${sourceFilePath2}: ${err2}`);
      process.exit(1);
    }

    // Concatenate the contents of the two source files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFilePath, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        console.error(`Error writing to ${destinationFilePath}: ${err3}`);
        process.exit(1);
      }
      console.log(`Concatenated files saved to ${destinationFilePath}`);
    });
  });
});
