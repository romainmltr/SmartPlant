const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

let humidity = 0;
app.get('/humidity', (req, res) => {
    res.send({ humidity: humidity });
});

app.post('/humidity', (req, res) => {
    const { value } = req.body;

    humidity = value;
    res.json({ humidity });
});

// Listen to port
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
