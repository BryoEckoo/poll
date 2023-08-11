#!/bin/bash

# Activate the virtual environment (if needed)
source polll/Scripts/activate  # Uncomment this line if using a virtual environment

# Install requirements (if not already installed)
python3.9 -m pip install -r requirements.txt

# Apply database migrations
python3.9 manage.py migrate

# No need to collectstatic if static files are already collected

# Deactivate the virtual environment (if needed)
# deactivate  # Uncomment this line if using a virtual environment
