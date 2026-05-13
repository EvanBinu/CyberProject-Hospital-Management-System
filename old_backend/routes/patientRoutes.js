const express = require('express');

const { body, validationResult } = require('express-validator');

const authMiddleware = require('../middleware/authMiddleware');
const roleMiddleware = require('../middleware/roleMiddleware');

const pool = require('../database/db');

const router = express.Router();

router.post(
    '/',
    authMiddleware,
    roleMiddleware('doctor', 'admin'),

    [
        body('patient_name')
            .trim()
            .escape()
            .isLength({ min: 2 }),

        body('age')
            .isInt({ min: 0, max: 120 }),

        body('diagnosis')
            .trim()
            .escape()
    ],

    async (req, res) => {

        const errors = validationResult(req);

        if (!errors.isEmpty()) {

            return res.status(400).json({
                errors: errors.array()
            });
        }

        const {
            patient_name,
            age,
            diagnosis
        } = req.body;

        try {

            await pool.query(
                `INSERT INTO patients
                (patient_name, age, diagnosis, doctor_id)
                VALUES($1, $2, $3, $4)`,

                [
                    patient_name,
                    age,
                    diagnosis,
                    req.user.id
                ]
            );

            res.json({
                message: 'Patient added securely'
            });

        } catch (err) {

            res.status(500).json({
                error: err.message
            });
        }
    }
);

router.get(
    '/',
    authMiddleware,

    async (req, res) => {

        try {

            const patients = await pool.query(
                'SELECT * FROM patients'
            );

            res.json(patients.rows);

        } catch (err) {

            res.status(500).json({
                error: err.message
            });
        }
    }
);
router.put(
    '/:id',

    authMiddleware,
    roleMiddleware('doctor', 'admin'),

    async (req, res) => {

        const { id } = req.params;

        const {
            patient_name,
            age,
            diagnosis
        } = req.body;

        try {

            await pool.query(
                `UPDATE patients
                 SET patient_name=$1,
                     age=$2,
                     diagnosis=$3
                 WHERE id=$4`,

                [
                    patient_name,
                    age,
                    diagnosis,
                    id
                ]
            );

            res.json({
                message: 'Patient updated securely'
            });

        } catch (err) {

            res.status(500).json({
                error: err.message
            });
        }
    }
);
router.delete(
    '/:id',

    authMiddleware,
    roleMiddleware('admin'),

    async (req, res) => {

        const { id } = req.params;

        try {

            await pool.query(
                'DELETE FROM patients WHERE id=$1',
                [id]
            );

            res.json({
                message: 'Patient deleted securely'
            });

        } catch (err) {

            res.status(500).json({
                error: err.message
            });
        }
    }
);
module.exports = router;