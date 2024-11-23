const axios = require('axios');
const config = require('./config.json');

const apiKey = config.AZURE_OPENAI_API_KEY;
const endpoint = config.AZURE_OPENAI_ENDPOINT;
const deployment = config.AZURE_OPENAI_DEPLOYMENT;
const version = config.AZURE_OPENAI_API_VERSION;

const messages = [
    { role: 'system', content: 'You are a helpful assistant.' },
    { role: 'user', content: 'tell me a joke' }
];

const requestBody = {
    messages: messages,
    max_tokens: 50
};

const headers = {
    'Content-Type': 'application/json',
    'api-key': `${apiKey}`
};

axios.post(`${endpoint}/openai/deployments/${deployment}/chat/completions?api-version=${version}`, requestBody, { headers })
    .then(response => {
        console.log('Response:', response.data.choices[0].message.content);
    })
    .catch(error => {
        console.error('Error:', error);
    });