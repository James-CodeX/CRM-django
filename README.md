# CRM Django Project

This is a Customer Relationship Management (CRM) system built with Django and MySQL.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- MySQL Server
- pip (Python package manager)

## Setup Instructions

1. Clone this repository:

```bash
git clone <repository-url>
cd CRM-django
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install django mysql-connector-python
```

4. Create the MySQL Database:

- Make sure MySQL Server is running on your system
- Update the database credentials in `mydb.py` if needed:
  ```python
  host='localhost'
  user='root'
  password='Password123.'  # Change this to your MySQL root password
  ```
- Run the database creation script:
  ```bash
  python mydb.py
  ```
  This will create a new database named 'dcrm'

5. Configure Django:

- Update the database settings in `settings.py` to match your MySQL credentials
- Run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

6. Create a superuser (admin):

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

The application should now be running at `http://127.0.0.1:8000/`

## Database Configuration (mydb.py)

The `mydb.py` script is used to create the MySQL database for this project. Here's how it works:

1. It uses the `mysql-connector-python` package to connect to MySQL
2. Connects to MySQL server using the specified credentials:
   - Host: localhost
   - User: root
   - Password: Password123. (change this to your MySQL root password)
3. Creates a new database named 'dcrm'

If you need to modify the database configuration:

1. Open `mydb.py`
2. Update the connection parameters as needed
3. Run the script using `python mydb.py`

