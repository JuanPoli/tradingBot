import fetch from 'node-fetch';

export default async function handler(req, res) {
  try {
    const response = await fetch('https://juancruzpoli-gmailcom-trading-bot.vercel.app/run-colab');
    const data = await response.json();
    res.status(200).send(data);
  } catch (error) {
    console.log(error);
    res.status(500).send('Error running Colab notebook');
  }
}
