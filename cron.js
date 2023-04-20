import fetch from 'node-fetch';

export default async function handler(req, res) {
  try {
    const response = await fetch('api/cron');
    const data = await response.json();
    res.status(200).send(data);
  } catch (error) {
    console.log(error);
    res.status(500).send('Error running Colab notebook');
  }
}