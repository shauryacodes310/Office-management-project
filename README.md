# Team Task Manager

A full-stack Team Task Manager web application built using Django + HTMX.

## Features

- User Authentication (Signup/Login/Logout)
- Role-Based Access Control (Admin / Member)
- Project Management
- Task Creation & Assignment
- Drag-and-Drop Task Status Updates
- Dashboard with Task Tracking
- Overdue Task Monitoring
- Django Admin Panel
- Responsive Bootstrap UI
- HTMX-powered Dynamic Interactions

---

## Tech Stack

### Backend
- Django
- Django ORM

### Frontend
- HTML
- Bootstrap 5
- HTMX

### Database
- SQLite3

### Deployment
- Railway

---

## Roles

### Admin
- Manage users
- Create projects
- Assign tasks
- Access admin panel

### Member
- View assigned tasks
- Update task status

---

## Project Structure

```bash
accounts/
projects/
tasks/
dashboard/
templates/
static/
config/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/rajanSaini12/office-management-system-ethara-ai.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## HTMX Integration

This project uses HTMX for:
- Dynamic task updates
- Partial page rendering
- Faster UI interactions without full page reloads

---

## Deployment

The application is deployed on Railway.

---

## Future Improvements

- Notifications
- Email reminders
- File attachments
- Activity logs
- Team chat integration

---

## Author

Rajan Saini
