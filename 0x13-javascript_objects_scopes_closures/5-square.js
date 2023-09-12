#!/usr/bin/node
/**
 * Class square that inherits from 4-rectangle.js
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor (size) {
        super(size, size);
    }
}

module.exports = Square;
