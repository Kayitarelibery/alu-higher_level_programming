#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    if (film.characters.some((character) => character.includes('/people/18/'))) {
      count += 1;
    }
  }

  console.log(count);
});
