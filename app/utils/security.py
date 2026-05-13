from flask_login import current_user

from flask import abort

def role_required(*roles):

    def wrapper(func):

        def decorated_function(*args, **kwargs):

            if current_user.role not in roles:

                abort(403)

            return func(*args, **kwargs)

        decorated_function.__name__ = func.__name__

        return decorated_function

    return wrapper
from app.models.audit_log import AuditLog

from app import db

from flask_login import current_user

def log_action(action):

    if current_user.is_authenticated:

        audit = AuditLog(

            username=current_user.username,

            action=action
        )

        db.session.add(audit)

        db.session.commit()