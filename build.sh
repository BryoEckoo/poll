 python3.9 polll\Scripts\activate.bat
 python3.9 -m pip install -r requirements.txt
 python3.9 python manage.py migrate
 python3.9 -m pip install whitenoise
 python3.9 manage.py collectstatic --noinput --clear
