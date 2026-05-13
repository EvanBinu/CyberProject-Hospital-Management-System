from app import db

class AuditLog(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100)
    )

    action = db.Column(
        db.String(255)
    )

    timestamp = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )