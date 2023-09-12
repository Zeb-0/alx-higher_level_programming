#!/usr/bin/node
/**
 * check no. of occurrences
 */
exports.nbOccurences = function (list, searchElement) {
  // Use the reduce method for counting occurrences
  const count = list.reduce((accumulator, currentElement) => {
    if (currentElement === searchElement) {
      return accumulator + 1;
    }
    return accumulator;
  }, 0);

  return count;
};
