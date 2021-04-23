# coursera-cybersecurity-capstone
Solution for [Coursera Cybersecurity Capstone Project](https://www.coursera.org/learn/cyber-security-capstone)


## Setup environment
```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Create project and apps
```
django-admin startproject chat_project
cd chat_project
django-admin startapp account
```

## Run the app

The easiest way to setup and run a full clean environment is by typing in the root project folder the following command:
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
Go to a website `http://127.0.0.1:8000/`

### Run a production server
First you need to install `nginx` server
```
sudo apt install nginx
touch /etc/nginx/sites-available/chat_project
cp chat_project/chat_project_nginx.conf /etc/nginx/sites-available/chat_project
sudo ln -s /etc/nginx/sites-available/chat_project /etc/nginx/sites-enabled
```
Check if created configuratin does not contain any bugs by typing:
```
sudo nginx -t
```
Modify a gunicorn run command to be able to talk to Nginx:
```
gunicorn --daemon --workers=5 --bind unix:~/chat_project/chat_project/chat_project.sock chat_project.wsgi
```
Modify /etc/nginx/nginx.conf as shown below:
```
user root www-data
```

```
gunicorn -b 0.0.0.0:8000 chat_project.wsgi
```

Restart Nginx:
```
systemctl restart nginx
```

### Go to a website
`http://127.0.0.1:8000/`