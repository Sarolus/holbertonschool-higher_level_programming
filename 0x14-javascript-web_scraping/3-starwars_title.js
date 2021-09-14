#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(api, { json: true }, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  console.log(body.title);
});
