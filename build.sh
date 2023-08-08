  python3.9 python -m venv venv
 python3.9 venv/Scripts/activate
 python3.9 -m pip install -r requirements.txt
 python3.9 python manage.py migrate
 python3.9 manage.py collectstatic --noinput --clear