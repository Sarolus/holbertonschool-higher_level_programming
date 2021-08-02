#!/usr/bin/node
const myString = 'C is fun';
const occurence = parseInt(process.argv[2]);

if (!occurence) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < occurence; i++) {
    console.log(myString);
  }
}
