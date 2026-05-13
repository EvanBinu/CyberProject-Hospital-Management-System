from flask import (
    Blueprint,
    render_template
)

from flask_login import (
    login_required
)

from app.models.audit_log import AuditLog

from app.utils.security import (
    role_required
)

audit_bp = Blueprint(
    'audit',
    __name__
)


@audit_bp.route('/audit-logs')

@login_required

@role_required('admin')

def audit_logs():

    logs = AuditLog.query.order_by(
        AuditLog.timestamp.desc()
    ).all()

    return render_template(
        'audit_logs.html',
        logs=logs
    )