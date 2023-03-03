const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

let humidity = 0;
let water = 0;

app.get('/humidity', (req, res) => {
    res.send({ humidity: humidity });
});

app.post('/humidity', (req, res) => {
    const { value } = req.body;
    humidity = value;
    res.json({ humidity });
});

app.get('/water', (req, res) => {
    res.send({ water: water });
    water = 0;
});


app.post('/water', (req, res) => {
    const { state } = req.body;

    if (state) {
        water = 1;
    } else {
        water = 0;
    }

     res.json({ water });
});

// Listen to port
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
