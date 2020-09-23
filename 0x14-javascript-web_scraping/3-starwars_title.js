#!/usr/bin/node

const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(URL, function (err, response, body) {
  const jsonObj = JSON.parse(body);
  console.log(jsonObj.title);
  if (err) {}
});
