
SHELL := /bin/bash

# Signifies our desired python version
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help setup test run clean all

# Defining an array variable
FILES =

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = all

# Run the app
all: setup run_prod

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

# This generates the desired project file structure
setup:
	${PYTHON} -m venv venv
	source venv/bin/activate && pip install -U pip && pip install -r requirements.txt

# This function uses pytest to test our source files, not used for now
test:
	${PYTHON} -m pytest

run_dev:
	source venv/bin/activate && cd chat_project && ${PYTHON} manage.py makemigrations && ${PYTHON} manage.py migrate && ${PYTHON} manage.py runserver

run_prod:
	source venv/bin/activate && cd chat_project && ${PYTHON} manage.py makemigrations && ${PYTHON} manage.py migrate && python manage.py collectstatic && gunicorn -b 0.0.0.0:8000 chat_project.wsgi


# Cleanup the stuff
clean:
	rm -r venv chat_project/db.sqlite3
