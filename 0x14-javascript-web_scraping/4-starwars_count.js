#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  let counter = 0;
  body.results.forEach(films => {
    films.characters.forEach(characters => {
      if (characters.indexOf('people/18') >= 0) {
        counter++;
      }
    });
  });
  console.log(counter);
});
