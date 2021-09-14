#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const user = {};
  body.forEach(element => {
    if (element.completed) {
      if (element.userId in user) {
        user[element.userId] += 1;
      } else {
        user[element.userId] = 1;
      }
    }
  });
  console.log(user);
});
