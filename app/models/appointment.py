from app import db

class Appointment(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_name = db.Column(
        db.String(100),
        nullable=False
    )

    doctor_name = db.Column(
        db.String(100),
        nullable=False
    )

    appointment_date = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default='Pending'
    )
    report_filename = db.Column(
        db.String(255)
    )