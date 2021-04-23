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
python manage.py runserver 127.0.0.1:8000
```
Go to a website `http://127.0.0.1:8000/`

### Run a production server
Test if gunicorn works
```
gunicorn -b 0.0.0.0:8000 chat_project.wsgi
```
Go to a website `http://0.0.0.0:8000/` and see if it is accessible.

First you need to install `nginx` server
```
sudo apt-get update
sudo apt install nginx
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default
touch /etc/nginx/sites-available/chat_project && cp chat_project/chat_project_nginx.conf /etc/nginx/sites-available/chat_project
mkdir -p  /root/Projects/coursera-cybersecurity-capstone/chat_project/logs && touch /root/Projects/coursera-cybersecurity-capstone/chat_project/logs/nginx-access.log

sudo ln -sf /etc/nginx/sites-available/chat_project /etc/nginx/sites-enabled
```

Modify `/etc/nginx/nginx.conf` as shown below:
```
user root www-data
```

Check if created configuratin does not contain any bugs by typing:
```
sudo nginx -t
```

Collect all the static files
```
python manage.py collectstatic
```

Modify a gunicorn run command to be able to talk to Nginx:
```
pkill gunicorn
gunicorn --daemon --workers=3 --bind unix:/tmp/chat_project.sock chat_project.wsgi
```

or preffered way:
```
pkill gunicorn
chmod a+x run_gunicorn.sh
./run_gunicorn.sh
```

Restart Nginx:
```
systemctl restart nginx
```

Go to a website `http://0.0.0.0:8000/`