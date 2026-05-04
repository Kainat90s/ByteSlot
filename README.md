<<<<<<< HEAD
# ByteSlot — Modular Scheduling System

A production-ready scheduling & booking platform built with Django + React.

## Tech Stack

| Layer      | Technology                            |
|------------|---------------------------------------|
| Backend    | Django 4.2, Django REST Framework     |
| Database   | MS SQL Server (mssql-django)          |
| Auth       | JWT (SimpleJWT)                       |
| Async      | Celery + Redis                        |
| Frontend   | React 18 (Vite), Tailwind CSS, Axios  |
| Meetings   | Google Calendar API (Meet links)      |

---

## Project Structure

```
byteslot/
├── backend/
│   ├── config/          # Django settings, URLs, Celery, WSGI/ASGI
│   ├── accounts/        # Custom User, JWT auth
│   ├── core/            # SystemSettings, Dashboard API
│   ├── availability/    # Slot management (weekend/overlap/buffer)
│   ├── bookings/        # Booking CRUD with validation pipeline
│   ├── notifications/   # Email + Celery tasks (confirm/cancel/reminder)
│   ├── integrations/    # Google OAuth 2.0 + Meet link creation
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── api/         # Axios instance with JWT interceptors
    │   ├── context/     # Auth context
    │   ├── components/  # Layout, Sidebar
    │   └── pages/       # Dashboard, Availability, Bookings, Settings, Login
    └── package.json
```

---

## Setup Guide

### Prerequisites
- Python 3.10+
- Node.js 18+
- MS SQL Server (Express or full)
- Redis (for Celery)
- ODBC Driver 17 for SQL Server

### 1. Database
Create the `byteslot` database in SQL Server:
```sql
CREATE DATABASE byteslot;
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Copy env file and configure
copy .env.example .env

# Run migrations
python manage.py makemigrations accounts core availability bookings notifications integrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Start server
python manage.py runserver
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

### 4. Celery (for notifications)
```bash
cd backend

# Start worker
celery -A config worker -l info

# Start beat (periodic tasks)
celery -A config beat -l info
```

---

## API Endpoints

| Method | Endpoint                          | Description              |
|--------|-----------------------------------|--------------------------|
| POST   | `/api/accounts/register/`         | Register new user        |
| POST   | `/api/accounts/login/`            | Login (returns JWT)      |
| GET    | `/api/accounts/profile/`          | Current user profile     |
| POST   | `/api/accounts/token/refresh/`    | Refresh JWT token        |
| GET    | `/api/core/dashboard/`            | Dashboard data           |
| GET/PUT| `/api/core/settings/`             | System settings          |
| GET    | `/api/availability/slots/`        | Public available slots   |
| GET/POST| `/api/availability/admin/slots/` | Admin slot management    |
| POST   | `/api/bookings/create/`           | Create booking           |
| GET    | `/api/bookings/`                  | List bookings            |
| POST   | `/api/bookings/:id/cancel/`       | Cancel booking           |
| GET    | `/api/integrations/google/auth/`  | Start Google OAuth       |
| GET    | `/api/integrations/google/status/`| Check Google connection  |

---

## Key Features

- **Weekend Exclusion**: Saturday & Sunday automatically marked OFF
- **Buffer Enforcement**: Configurable buffer before/after meetings
- **Overlap Prevention**: No double-booking allowed
- **Google Meet**: Auto-generated Meet links for video bookings
- **Email Notifications**: Confirmation, cancellation, 1-hour reminders
- **Dashboard**: Weekly hours summary, upcoming meetings, booking stats
=======
# ByteSlot
>>>>>>> c6fda5687f776230c95b95412d636ad7154cc248
