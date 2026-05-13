from flask import Blueprint, render_template

from flask_login import (
    login_required,
    current_user
)

from app.models.patient import Patient

from app.models.appointment import Appointment

dashboard_bp = Blueprint(
    'dashboard',
    __name__
)

@dashboard_bp.route('/dashboard')

@login_required

def dashboard():

    total_patients = Patient.query.count()

    total_appointments = (
        Appointment.query.count()
    )

    return render_template(
        'dashboard.html',
        total_patients=total_patients,
        total_appointments=total_appointments,
        current_user=current_user
    )