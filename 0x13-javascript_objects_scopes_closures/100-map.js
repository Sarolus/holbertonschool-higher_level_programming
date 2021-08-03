#!/usr/bin/node
let index = 0;
const list = require('./100-data.js').list;

console.log(list);
const map1 = list.map(x => x * index++);
console.log(map1);
