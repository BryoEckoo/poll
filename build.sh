#!/bin/bash

# Create a virtual environment and activate it
python -m venv venv
venv/Script/activate.bat

# Install the requirements
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the Django development server (you may need to adjust the host and port as per Vercel's requirements)
python manage.py runserver 0.0.0.0:8000
