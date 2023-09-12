#!/usr/bin/node
/**
 * Rectangle handle incorrect dimensions
 */
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not a positive integer or equal to 0
      this.width = undefined;
      this.height = undefined;
    }
  }
}
module.exports = Rectangle
