const fetch = require('node-fetch');

fetch('https://trading-bot-swart.vercel.app/run-colab')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

