#!/bin/bash

# Create and activate the virtual environment
python3.9 -m venv polll
source polll/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput --clear

# Deactivate the virtual environment
deactivate
