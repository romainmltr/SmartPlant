const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

app.get('/Test', (req, res) => {
    res.set('Content-Type', 'text/html');
    res.send('Hello world !!');
});

// Create Array
const humidityData = [];
// Add Data
app.post('/humidity', (req, res) => {
    const { humidity } = req.body;
    humidityData.push(humidity);

    // Send back data
    res.json(humidityData);
    console.log(humidityData);
});

app.post('/water', (req, res) => {
    const { state } = req.body;

    // Activez
    if (state) {
        // Code pour activer l'eau
    } else {
        // Code pour désactiver l'eau
    }

    // Renvoyer l'état de l'eau dans la réponse JSON
    res.json({ state });
});


// Listen to port
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
