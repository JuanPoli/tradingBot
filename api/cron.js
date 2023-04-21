const fetch = require('node-fetch');

console.log("Starting cron job...");

fetch('https://trading-bot-swart.vercel.app/run-colab')
  .then(response => {
    console.log("Response status: " + response.status);
    return response.json();
  })
  .then(data => {
    console.log("Response data: " + JSON.stringify(data));
  })
  .catch(error => {
    console.error("Error: " + error);
  });

