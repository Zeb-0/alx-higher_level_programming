#!/usr/bin/node
/**
 * Square class that inherits from 5-squre.js class square
 */
const child_sqaure = require('./5-square');

class Square extends child_sqaure {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
