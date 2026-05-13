# Secure Hospital Management System (Flask + Jinja + SQLite)

## Overview

The Secure Hospital Management System (Secure HMS) is a cybersecurity-focused full-stack web application developed using Flask, Jinja2 templates, SQLite, and SQLAlchemy ORM.

The project was designed as a secure healthcare management platform that demonstrates:

* secure authentication
* role-based access control
* secure CRUD operations
* secure file uploads
* audit logging
* session security
* SQL injection protection
* cybersecurity best practices

The system simulates a hospital environment where administrators, doctors, and receptionists can securely manage patients, appointments, and medical reports.

---

# Technology Stack

| Component             | Technology               |
| --------------------- | ------------------------ |
| Backend Framework     | Flask                    |
| Frontend              | Jinja2 Templates         |
| Database              | SQLite                   |
| ORM                   | SQLAlchemy               |
| Authentication        | Flask-Login              |
| Password Hashing      | Flask-Bcrypt             |
| Security Headers      | Flask-Talisman           |
| CSRF Protection       | Flask-WTF                |
| Environment Variables | python-dotenv            |
| File Upload Security  | Werkzeug secure_filename |
| UI Framework          | Bootstrap 5              |
| Logging               | Custom Audit Logging     |

---

# Features Implemented

## 1. Secure Authentication System

The project includes a fully functional secure authentication system.

### Features

* User Registration
* User Login
* User Logout
* Session Management
* Password Hashing
* Protected Routes
* Login Validation
* Duplicate User Prevention

### Security Features

* Passwords are hashed using bcrypt
* Sessions handled securely using Flask-Login
* Unauthorized users blocked from protected routes
* Duplicate usernames and emails prevented

### Routes

| Route     | Description        |
| --------- | ------------------ |
| /register | Register new users |
| /login    | User login         |
| /logout   | User logout        |

---

# 2. Role-Based Access Control (RBAC)

The system supports multiple user roles.

## Roles

| Role         | Permissions                      |
| ------------ | -------------------------------- |
| Admin        | Full system access               |
| Doctor       | Manage patients and appointments |
| Receptionist | Manage appointments only         |

### Security Benefits

* Principle of least privilege
* Restricted access to sensitive operations
* Prevents unauthorized actions

### Role Restrictions

| Feature         | Admin | Doctor | Receptionist |
| --------------- | ----- | ------ | ------------ |
| Add Patient     | Yes   | Yes    | No           |
| Delete Patient  | Yes   | No     | No           |
| Add Appointment | Yes   | Yes    | Yes          |
| Upload Reports  | Yes   | Yes    | No           |
| View Audit Logs | Yes   | No     | No           |

---

# 3. Patient Management Module

The application contains a complete patient management system.

## Features

* Add Patient
* View Patients
* Edit Patient
* Delete Patient

## Security Features

* Protected CRUD routes
* Role-based restrictions
* SQL injection protection through ORM
* Authenticated access only

## Patient Fields

* Patient Name
* Age
* Diagnosis

---

# 4. Appointment Management Module

The appointment management system allows scheduling and managing hospital appointments.

## Features

* Add Appointment
* View Appointments
* Edit Appointment
* Delete Appointment
* Appointment Status Updates

## Appointment Fields

* Patient Name
* Doctor Name
* Appointment Date
* Status

## Appointment Status Options

* Pending
* Completed
* Cancelled

---

# 5. Secure Medical Report Upload System

A secure medical report upload system was implemented.

## Features

* Upload medical reports
* Upload PDF/image files
* View uploaded reports
* Associate reports with appointments

## Supported File Types

* PDF
* PNG
* JPG
* JPEG

## Security Features

### File Validation

Only approved file extensions are allowed.

### Secure Filenames

The system uses:

```python
secure_filename()
```

to prevent path traversal attacks.

### Unique File Storage

UUID-based filenames prevent overwriting.

### File Size Limiting

Uploads restricted using:

```python
MAX_CONTENT_LENGTH
```

### Role Protection

Only admins and doctors can upload reports.

---

# 6. Audit Logging System

The system contains a complete audit logging mechanism.

## Logged Events

* User Login
* User Logout
* User Registration
* Patient Add/Edit/Delete
* Appointment Add/Edit/Delete
* Report Uploads

## Audit Log Fields

| Field     | Description            |
| --------- | ---------------------- |
| Username  | User performing action |
| Action    | Event performed        |
| Timestamp | Time of event          |

## Security Benefits

* Accountability
* Activity Monitoring
* Forensic Analysis
* Administrative Oversight
* Healthcare Compliance Simulation

---

# 7. Dashboard System

The project includes a Bootstrap-based admin dashboard.

## Dashboard Features

* Total Patients Counter
* Total Appointments Counter
* Current User Role Display
* Navigation Bar
* Responsive UI

---

# 8. Bootstrap UI Integration

Bootstrap 5 was integrated for a professional responsive interface.

## UI Features

* Responsive Navbar
* Styled Forms
* Responsive Tables
* Dashboard Cards
* Flash Messages
* Mobile-Friendly Layout

---

# 9. SQLAlchemy ORM Security

The application uses SQLAlchemy ORM instead of raw SQL queries.

## Benefits

* Prevents SQL injection
* Cleaner database code
* Easier CRUD operations
* Better maintainability
* Relationship support

Example:

```python
User.query.filter_by(email=email).first()
```

instead of raw SQL.

---

# 10. Session Security

The application uses Flask-Login for secure session handling.

## Features

* User sessions
* Protected routes
* Automatic login management
* Logout support
* Session persistence

---

# 11. Password Security

Passwords are securely hashed using bcrypt.

## Benefits

* Passwords never stored in plaintext
* Resistant to rainbow table attacks
* Strong hashing algorithm

Example:

```python
bcrypt.generate_password_hash(password)
```

---

# 12. CSRF Protection

CSRF protection is enabled using Flask-WTF.

## Protection Against

* Cross-site request forgery attacks
* Unauthorized form submissions

---

# 13. Security Headers

The application uses Flask-Talisman.

## Security Headers Added

* Content Security Policy
* Strict Transport Security
* X-Frame-Options
* X-Content-Type-Options

## Benefits

* Prevents clickjacking
* Improves browser security
* Enhances secure communication

---

# 14. Project Structure

```text
CyberProject-Hospital-Management-System/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── utils/
│
├── instance/
│   └── hospital.db
│
├── requirements.txt
├── config.py
├── run.py
├── .env
└── README.md
```

---

# Database Models

## User Model

Fields:

* username
* email
* password
* role

## Patient Model

Fields:

* patient_name
* age
* diagnosis

## Appointment Model

Fields:

* patient_name
* doctor_name
* appointment_date
* status
* report_filename

## AuditLog Model

Fields:

* username
* action
* timestamp

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone <repository-url>
```

## Step 2 — Navigate Into Project

```bash
cd CyberProject-Hospital-Management-System
```

## Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

## Step 4 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 6 — Configure Environment Variables

Create:

```text
.env
```

Add:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///hospital.db
```

## Step 7 — Run Application

```bash
python run.py
```

## Step 8 — Open Browser

```text
http://127.0.0.1:5000
```

---

# Security Features Summary

| Feature                  | Implemented |
| ------------------------ | ----------- |
| Authentication           | Yes         |
| RBAC                     | Yes         |
| Secure Password Hashing  | Yes         |
| SQL Injection Protection | Yes         |
| CSRF Protection          | Yes         |
| Security Headers         | Yes         |
| Secure Upload Validation | Yes         |
| Audit Logging            | Yes         |
| Session Management       | Yes         |
| Secure File Handling     | Yes         |

---

# Future Improvements

The following advanced features are planned for future development.

## 1. Rate Limiting

Using Flask-Limiter to prevent:

* brute force attacks
* API abuse
* spam requests

---

## 2. Flask-WTF Secure Forms

Replace manual forms with:

* WTForms validation
* automatic CSRF tokens
* better input validation

---

## 3. Search and Filtering

Add:

* patient search
* appointment filtering
* doctor filtering
* date filtering

---

## 4. Dashboard Analytics

Add charts and statistics.

Possible tools:

* Chart.js
* Plotly
* ApexCharts

---

## 5. Pagination

Add pagination for:

* patients
* appointments
* audit logs

for better performance.

---

## 6. Email Notifications

Send emails for:

* appointment confirmations
* reminders
* password reset

---

## 7. Session Timeout

Automatically log out inactive users.

---

## 8. Docker Deployment

Containerize application using Docker.

---

## 9. HTTPS Deployment

Deploy using:

* Nginx
* Gunicorn
* SSL certificates

---

## 10. REST API Integration

Future API endpoints for:

* mobile applications
* external systems
* microservices

---

## 11. Real Database Migration

Move from SQLite to:

* PostgreSQL
* MySQL

for production deployment.

---

## 12. Advanced Security Features

Potential additions:

* Two-factor authentication
* JWT authentication
* Account lockout
* Intrusion detection
* Security monitoring
* Encrypted medical records

---

# Learning Outcomes

This project demonstrates practical implementation of:

* secure software engineering
* Flask web development
* database management
* authentication systems
* secure file handling
* RBAC systems
* audit logging
* cybersecurity best practices

---

# Disclaimer

This project is an educational cybersecurity-focused hospital management system prototype.

It should not be used in real healthcare environments without:

* professional security audits
* encryption compliance
* regulatory compliance
* production-grade infrastructure
* proper authentication hardening

---

# Author

Evan Binu

B.Tech Computer Science

Cybersecurity & Full Stack Development Project
