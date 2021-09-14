#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(process.argv[3], body, error => {
    if (error) {
      return console.error(error);
    }
  });
});
