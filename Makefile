SHELL := /bin/bash

# Signifies our desired python version
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = all

# Defining an array variable
FILES =

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = all

# App main directory
APP_DIR = $(shell pwd)/chat_project
export APP_DIR

# Setup and run the app
all: setup run

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup [prod=on] for production"
	@echo "To test the project type make test"
	@echo "To run the project type make run [prod=on] for production"
	@echo "------------------------------------"

# This generates the desired project file structure
setup:
ifdef prod # PROD_MODE
	${PYTHON} -m venv venv
	source venv/bin/activate &&	\
	pip install -U pip &&	\
	pip install -r requirements.txt &&	\
	sudo apt-get update &&	\
	sudo apt install nginx &&	\
	sudo rm -rf /etc/nginx/sites-available/default &&	\
	sudo rm -rf /etc/nginx/sites-enabled/default &&	\
	touch /etc/nginx/sites-available/chat_project &&	\
	cp chat_project/chat_project_nginx.conf /etc/nginx/sites-available/chat_project &&	\
	mkdir -p chat_project/logs &&	\
	touch chat_project/logs/nginx-access.log && \
	sudo ln -sf /etc/nginx/sites-available/chat_project /etc/nginx/sites-enabled

else # DEV_MODE
	${PYTHON} -m venv venv
	source venv/bin/activate && \
	pip install -U pip && pip install -r requirements.txt

endif

run:
ifdef prod # PROD_MODE
	sed -i 's/DEBUG =.*/DEBUG = False/g' chat_project/chat_project/settings.py
	source venv/bin/activate &&	\
	cd chat_project &&	\
	python manage.py makemigrations &&	\
	python manage.py migrate &&	\
	python manage.py collectstatic &&	\
	chmod a+x run_gunicorn.sh &&	\
	./run_gunicorn.sh $(APP_DIR) && \
	systemctl restart nginx
	@echo "Production server started running at: 127.0.0.1:80"

else # DEV_MODE
	@echo $(APP_DIR)
	sed -i 's/DEBUG =.*/DEBUG = True/g' chat_project/chat_project/settings.py
	source venv/bin/activate &&	\
	cd chat_project &&	\
	python manage.py makemigrations &&	\
	python manage.py migrate &&	\
	python manage.py runserver 127.0.0.1:8000
	@echo "Development server started running at: 127.0.0.1:8000"

endif

# This function uses pytest to test our source files, not used for now
test:
	${PYTHON} -m pytest

# Cleanup the stuff
clean:
	rm -r venv chat_project/db.sqlite3
