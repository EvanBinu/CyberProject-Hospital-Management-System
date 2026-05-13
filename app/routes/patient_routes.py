from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from app.utils.security import log_action
from flask_login import login_required

from app import db, csrf

from app.models.patient import Patient
from app.utils.security import role_required
patient_bp = Blueprint(
    'patients',
    __name__
)

@patient_bp.route('/patients')

@login_required

def patients():

    all_patients = Patient.query.all()

    return render_template(
        'patients.html',
        patients=all_patients
    )


@patient_bp.route(
    '/add-patient',
    methods=['POST']
)
@login_required

@csrf.exempt

@role_required('admin', 'doctor')

def add_patient():

    patient_name = request.form['patient_name']

    age = request.form['age']

    diagnosis = request.form['diagnosis']

    patient = Patient(
        patient_name=patient_name,
        age=age,
        diagnosis=diagnosis
    )

    db.session.add(patient)

    db.session.commit()
    log_action(
        f'Added Patient: {patient_name}'
    )
    flash('Patient Added Successfully')

    return redirect(
        url_for('patients.patients')
    )


@patient_bp.route('/delete-patient/<int:id>')

@login_required

@role_required('admin')
def delete_patient(id):

    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)

    db.session.commit()
    log_action(
        f'Deleted Patient: {patient.patient_name}'
    )
    flash('Patient Deleted')

    return redirect(
        url_for('patients.patients')
    )
@patient_bp.route(
    '/edit-patient/<int:id>',
    methods=['GET', 'POST']
)

@login_required

@csrf.exempt

@role_required('admin', 'doctor')

def edit_patient(id):

    patient = Patient.query.get_or_404(id)

    if request.method == 'POST':

        patient.patient_name = request.form[
            'patient_name'
        ]

        patient.age = request.form['age']

        patient.diagnosis = request.form[
            'diagnosis'
        ]

        db.session.commit()
        log_action(
            f'Edited Patient: {patient.patient_name}'
        )
        flash('Patient Updated')

        return redirect(
            url_for('patients.patients')
        )

    return render_template(
        'edit_patient.html',
        patient=patient
    )