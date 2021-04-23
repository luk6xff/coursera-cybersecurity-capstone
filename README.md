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

The easiest way to setup and run a full clean environment is by typing in the root:
```
make
```

### Build
```
source venv/bin/activate
cd chat_project
python manage.py makemigrations && python manage.py migrate
```

### Create an admin account
```
python manage.py createsuperuser --username=luk6xff --email=luk6xff@example.com
$ password: ...
```

### Run a development server
```
python manage.py runserver
```

### Run a production server
TODO

### Go to a website
`http://127.0.0.1:8000/`