# Virtual Call Tracker

A Django project to track calls, view them via an interactive dashboard, and access call data through a REST API.

---

## Features

- **CRUD operations** for calls using Django Admin
- **REST API** for call data (GET, POST, PUT, DELETE)
- **Interactive Dashboard**:
  - Filter calls by status: missed, completed, ongoing
  - Colored status badges for easy visualization
- **Automatic timestamps** for created and updated calls

---

## Tech Used

- Django 5.2.7
- Django REST Framework  
- Bootstrap 5  
- JavaScript (for dashboard filters)  



# Getting Started

### 1. Clone the repository

git clone https://github.com/NadineMacDonald222/virtual-call-tracker.git
cd virtual-call-tracker

### 2. Create & activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create superuser (for admin)
python manage.py createsuperuser

### 6. Run server
python manage.py runserver

### 7. Access the project
- Admin Panel: http://127.0.0.1:8000/admin/

- API Calls: http://127.0.0.1:8000/api/calls/

- Dashboard: http://127.0.0.1:8000/dashboard/
