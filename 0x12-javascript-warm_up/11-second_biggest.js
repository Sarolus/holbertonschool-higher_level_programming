#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const array = process.argv.slice(2);
  const intArray = array.map(Number);
  intArray.sort((a, b) => a - b);
  console.log(intArray[intArray.length - 2]);
}
