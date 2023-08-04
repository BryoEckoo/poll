#!/bin/bash

# Create a virtual environment and activate it
Python3.11.4 python -m venv venv
Python3.11.4 source venv/bin/activate

# Install the requirements
Python3.11.4 pip install -r requirements.txt
python3.11.4  manage.py collectstatic --noinput --clear

# Run database migrations
Python3.11.4 python manage.py migrate

# Start the Django development server (you may need to adjust the host and port as per Vercel's requirements)

