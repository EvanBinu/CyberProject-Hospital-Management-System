from app import db

class Patient(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patient_name = db.Column(
        db.String(100),
        nullable=False
    )

    age = db.Column(db.Integer)

    diagnosis = db.Column(db.Text)