# coursera-cybersecurity-capstone
Solution for [Coursera Cybersecurity Capstone Project](https://www.coursera.org/learn/cyber-security-capstone)


## Setup environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create project and apps
```
django-admin startproject chat_project
cd chat_project
django-admin startapp account
```

## Run the app

### Build
```
cd chat_project
python manage.py makemigrations
python manage.py migrate
```

### Run a development server
```
python manage.py runserver
```
Go to: `http://127.0.0.1:8000/`

### Run a production server