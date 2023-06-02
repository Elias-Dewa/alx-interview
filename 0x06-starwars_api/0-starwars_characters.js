#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const request = require('request');

if (process.argv.length === 3) {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

  // Making API requests
  request(url, async (error, res, body) => {
    if (error) {
      console.log(error);
    } else {
      // each character url
      const urlList = JSON.parse(body).characters;

      // Get all characters
      for (const chars of urlList) {
        const answer = () => {
          return new Promise((resolve, reject) => {
            request(chars, async (error, res, body) => {
              if (error) {
                console.log(error);
              }
              resolve(JSON.parse(body).name);
            });
          });
        };
        console.log(await answer());
      }
    }
  });
}
