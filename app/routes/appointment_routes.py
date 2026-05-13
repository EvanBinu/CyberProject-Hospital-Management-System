from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

import os
import uuid

from werkzeug.utils import secure_filename

from flask_login import login_required

from app import db, csrf

from app.models.appointment import Appointment

from app.utils.validators import allowed_file
from app import limiter
from app.utils.security import (
    role_required,
    log_action
)

appointment_bp = Blueprint(
    'appointments',
    __name__
)


@appointment_bp.route('/appointments')

@login_required

def appointments():

    all_appointments = Appointment.query.all()

    return render_template(
        'appointments.html',
        appointments=all_appointments
    )


@appointment_bp.route(
    '/add-appointment',
    methods=['POST']
)

@login_required

@csrf.exempt

@role_required(
    'admin',
    'doctor',
    'receptionist'
)

def add_appointment():

    patient_name = request.form['patient_name']

    doctor_name = request.form['doctor_name']

    appointment_date = request.form[
        'appointment_date'
    ]

    appointment = Appointment(
        patient_name=patient_name,
        doctor_name=doctor_name,
        appointment_date=appointment_date
    )

    db.session.add(appointment)

    db.session.commit()

    log_action(
        f'Added Appointment for {patient_name}'
    )

    flash('Appointment Added')

    return redirect(
        url_for('appointments.appointments')
    )


@appointment_bp.route(
    '/delete-appointment/<int:id>'
)

@login_required

@role_required(
    'admin',
    'doctor'
)

def delete_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    db.session.delete(appointment)

    db.session.commit()

    log_action(
        f'Deleted Appointment ID {id}'
    )

    flash('Appointment Deleted')

    return redirect(
        url_for('appointments.appointments')
    )


@appointment_bp.route(
    '/edit-appointment/<int:id>',
    methods=['GET', 'POST']
)

@login_required

@csrf.exempt

@role_required(
    'admin',
    'doctor',
    'receptionist'
)

def edit_appointment(id):

    appointment = Appointment.query.get_or_404(id)

    if request.method == 'POST':

        appointment.patient_name = request.form[
            'patient_name'
        ]

        appointment.doctor_name = request.form[
            'doctor_name'
        ]

        appointment.appointment_date = request.form[
            'appointment_date'
        ]

        appointment.status = request.form[
            'status'
        ]

        db.session.commit()

        log_action(
            f'Edited Appointment ID {id}'
        )

        flash('Appointment Updated')

        return redirect(
            url_for(
                'appointments.appointments'
            )
        )

    return render_template(
        'edit_appointment.html',
        appointment=appointment
    )


@appointment_bp.route(
    '/upload-report/<int:id>',
    methods=['GET', 'POST']
)

@login_required

@csrf.exempt

@role_required(
    'admin',
    'doctor'
)
@limiter.limit(
    '10 per minute'
)
def upload_report(id):

    appointment = Appointment.query.get_or_404(id)

    if request.method == 'POST':

        if 'report' not in request.files:

            flash('No file selected')

            return redirect(request.url)

        file = request.files['report']

        if file.filename == '':

            flash('No file selected')

            return redirect(request.url)

        if (
            file and
            allowed_file(file.filename)
        ):

            unique_filename = (
                str(uuid.uuid4()) +
                "_" +
                secure_filename(
                    file.filename
                )
            )

            file_path = os.path.join(
                current_app.config[
                    'UPLOAD_FOLDER'
                ],
                unique_filename
            )

            file.save(file_path)

            appointment.report_filename = (
                unique_filename
            )

            db.session.commit()

            log_action(
                f'Uploaded Report: {unique_filename}'
            )

            flash('Report Uploaded')

            return redirect(
                url_for(
                    'appointments.appointments'
                )
            )

        flash('Invalid File Type')

        return redirect(request.url)

    return render_template(
        'upload_report.html',
        appointment=appointment
    )