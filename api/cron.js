import fetch from 'node-fetch';

export default async function handler(req, res) {
  try {
    const response = await fetch('https://trading-bot-swart.vercel.app/run-colab');
    const data = await response.json();
    if (response.ok && data.message === 'colab notebook ran successfully') {
      res.status(200).send(data);
    } else {
      res.status(500).send(data.message);
    }
  } catch (error) {
    console.log(error);
    res.status(500).send('Error running Colab notebook');
  }
}

