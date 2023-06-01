#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const request = require('request');

const movieId = process.env.splice(2)
const url = `https://swapi-api.alx-tools.com/api/${movieId[0]}/`;

// Making API requests
request(url, async (error, res, body) => {
  if (error) throw new Error(error);

  // each character url
  const urlList = JSON.parse(body).characters;

  // Get all characters
  for (let chars of urlList) {
    await new Promise((resolve, reject) => {
      request(chars, async (error, res, body) => {
        if (error) throw new Error(error);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});