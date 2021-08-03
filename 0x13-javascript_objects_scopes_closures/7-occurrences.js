#!/usr/bin/node
exports.nbOccurence = function (list, searchElement) {
  let i = 0;
  list.forEach(x => {
    if (x === searchElement) {
      i++;
    }
  });
  return i;
};
