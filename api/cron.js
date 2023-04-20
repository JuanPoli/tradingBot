const fetch = require('node-fetch');

module.exports = (req, res) => {
  fetch('https://trading-bot-swart.vercel.app/run-colab')
    .then((response) => {
      console.log('Colab executed successfully!');
      res.status(200).send('Colab executed successfully!');
    })
    .catch((error) => {
      console.error('Failed to execute Colab:', error);
      res.status(500).send('Failed to execute Colab');
    });
};

