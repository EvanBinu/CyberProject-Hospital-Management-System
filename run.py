from app import create_app, db

from app.models.user import User

from app.models.patient import Patient
from app.models.appointment import Appointment  
from app.models.audit_log import AuditLog
app = create_app()

with app.app_context():

    db.create_all()

if __name__ == '__main__':

    app.run(debug=True)