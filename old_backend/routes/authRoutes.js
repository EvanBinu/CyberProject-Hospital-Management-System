const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const { body, validationResult } = require('express-validator');

const pool = require('../database/db');

const router = express.Router();

router.post(
    '/register',
    [
        body('name').trim().escape(),
        body('email').isEmail(),
        body('password').isLength({ min: 8 }),
    ],

    async (req, res) => {

        const errors = validationResult(req);

        if (!errors.isEmpty()) {

            return res.status(400).json({
                errors: errors.array()
            });
        }

        const {
            name,
            email,
            password,
            role
        } = req.body;

        try {

            const existingUser = await pool.query(
                'SELECT * FROM users WHERE email=$1',
                [email]
            );

            if (existingUser.rows.length > 0) {

                return res.status(400).json({
                    message: 'User already exists'
                });
            }

            const hashedPassword = await bcrypt.hash(
                password,
                12
            );

            await pool.query(
                `INSERT INTO users(name, email, password, role)
                 VALUES($1, $2, $3, $4)`,
                [name, email, hashedPassword, role]
            );

            res.json({
                message: 'User registered securely'
            });

        } catch (err) {

            res.status(500).json({
                error: err.message
            });
        }
    }
);

router.post('/login', async (req, res) => {

    const { email, password } = req.body;

    try {

        const user = await pool.query(
            'SELECT * FROM users WHERE email=$1',
            [email]
        );

        if (user.rows.length === 0) {

            return res.status(401).json({
                message: 'Invalid credentials'
            });
        }

        const validPassword = await bcrypt.compare(
            password,
            user.rows[0].password
        );

        if (!validPassword) {

            return res.status(401).json({
                message: 'Invalid credentials'
            });
        }

        const token = jwt.sign(
            {
                id: user.rows[0].id,
                role: user.rows[0].role
            },
            process.env.JWT_SECRET,
            {
                expiresIn: '1h'
            }
        );

        res.json({
            token
        });

    } catch (err) {

        res.status(500).json({
            error: err.message
        });
    }
});

module.exports = router;