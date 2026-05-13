from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from flask_bcrypt import Bcrypt

from flask_wtf.csrf import CSRFProtect

from flask_talisman import Talisman

from dotenv import load_dotenv

import os

db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()

csrf = CSRFProtect()


def create_app():

    load_dotenv()

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv(
        'SECRET_KEY'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        os.getenv('DATABASE_URL')
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = (
        'app/static/uploads/reports'
    )

    app.config['MAX_CONTENT_LENGTH'] = (
        5 * 1024 * 1024
    )
    db.init_app(app)

    bcrypt.init_app(app)

    login_manager.init_app(app)

    csrf.init_app(app)

    Talisman(app)

    login_manager.login_view = 'auth.login'

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    from app.routes.auth_routes import auth_bp

    from app.routes.patient_routes import patient_bp

    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.appointment_routes import appointment_bp
    from app.routes.audit_routes import audit_bp
    
    app.register_blueprint(auth_bp)

    app.register_blueprint(patient_bp)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(audit_bp)
    @app.errorhandler(403)

    def forbidden(error):

        return render_template(
            '403.html'
        ), 403
    return app