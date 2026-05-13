from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from app import csrf
from app import db, bcrypt

from app.utils.security import log_action

from app.models.user import User

auth_bp = Blueprint(
    'auth',
    __name__
)


@auth_bp.route(
    '/register',
    methods=['GET', 'POST']
)

@csrf.exempt

def register():

    if request.method == 'POST':

        username = request.form['username']

        email = request.form['email']

        password = request.form['password']

        existing_user_email = User.query.filter_by(
            email=email
        ).first()

        existing_user_username = User.query.filter_by(
            username=username
        ).first()

        if existing_user_email:

            flash('Email already exists')

            return redirect(
                url_for('auth.register')
            )

        if existing_user_username:

            flash('Username already exists')

            return redirect(
                url_for('auth.register')
            )

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode('utf-8')

        user = User(
            username=username,
            email=email,
            password=hashed_password,
            role=request.form['role']
        )

        db.session.add(user)

        db.session.commit()

        log_action(
            f'New User Registered: {username}'
        )

        flash('Registration Successful')

        return redirect(
            url_for('auth.login')
        )

    return render_template(
        'register.html'
    )


@auth_bp.route(
    '/login',
    methods=['GET', 'POST']
)

@csrf.exempt

def login():

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        user = User.query.filter_by(
            email=email
        ).first()

        if (
            user and
            bcrypt.check_password_hash(
                user.password,
                password
            )
        ):

            login_user(user)

            log_action(
                'User Logged In'
            )

            flash('Login Successful')

            return redirect(
                url_for(
                    'dashboard.dashboard'
                )
            )

        flash('Invalid Credentials')

    return render_template(
        'login.html'
    )


@auth_bp.route('/logout')

@login_required

def logout():

    log_action(
        'User Logged Out'
    )

    logout_user()

    flash('Logged out successfully')

    return redirect(
        url_for('auth.login')
    )