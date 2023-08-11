#!/bin/bash

# Create and activate the virtual environment
source polll/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput --clear
