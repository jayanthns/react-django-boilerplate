REQUIREMENTS:
Django==1.11
djangorestframework==3.8.2

SETUP
1. virtualenv -p python3.6 env (setup virtual environment)
2. source env/bin/activate
2. git clone https://github.com/jayanthns/react-django-boilerplate.git
3. cd react-django-boilerplate
4. cd backend_app
5. pip install -r requirements.txt
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py createsuperuser
9. cd ..
10. cd frontend_app
11. yarn install or npm install
12. yarn collect or npm run collect
13. cd ..
14. python manage.py runserver 0.0.0.0:8000