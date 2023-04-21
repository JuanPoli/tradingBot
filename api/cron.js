const fetch = require('node-fetch');

fetch('https://trading-bot-swart.vercel.app/run-colab')
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Response not OK');
    }
  })
  .then(data => console.log(data))
  .catch(error => console.error(error));

