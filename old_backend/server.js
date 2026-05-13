require('dotenv').config();

const express = require('express');
const helmet = require('helmet');
const cors = require('cors');

const authRoutes = require('./routes/authRoutes');
const patientRoutes = require('./routes/patientRoutes');

const app = express();

app.use(express.json());

app.use(helmet());

app.use(cors());

app.use('/api/auth', authRoutes);
app.use('/api/patients', patientRoutes);

app.get('/', (req, res) => {

    res.send('Secure Hospital Management System Running');
});

app.listen(5000, () => {

    console.log('Server running on port 5000');
});