# Calorie Counter

A Django web application for tracking daily calorie intake.

## Features

- Add food items with calorie counts
- View all food items added today
- Remove individual food items
- Track progress toward a 2000 kcal daily goal with a progress bar
- Reset the daily calorie count
- Toast notifications for all actions

## Tech Stack

- Python 3.x / Django 6
- PostgreSQL
- Tailwind CSS
- Deployed on Render

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/winstone-1/calorie-counter-max.git
cd calorie-counter-max
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate       # Mac/Linux
```

### 3. Install dependencies
```bash
pip freeze > requirements.txt
```

### 4. Create .env file
- SECRET_KEY=your_secret_key
- DEBUG=True
- DB_NAME=calorie_db
- DB_USER=postgres
- DB_PASSWORD=your_password
- DB_HOST=localhost
- DB_PORT=5432

### 5. Create PostgreSQL database
```bash
psql -U postgres
CREATE DATABASE calorie_db;
\q
```

### 6. Run migrations
```bash
python manage.py migrate
```

### 7. Create superuser
```bash
python manage.py createsuperuser
```

### 8. Run the server
```bash
python manage.py runserver
```

## Live Site

[]()

## Deployment

Deployed on Render using PostgreSQL add-on. See `requirements.txt` for dependencies.
