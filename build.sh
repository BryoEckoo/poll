 python3.9 polll\Scripts\activate.bat
 pip install whitenoise
 pip freeze > requirements.txt
 pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 python3.9 python manage.py migrate