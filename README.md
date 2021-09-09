## Setup

after cloning the repo ru

```
pipenv install
```
Create a super user of the application

```
python manage.py createsuperuser
```

run the migrations

 ```
python manage.py makemigrations api_bookmark

python manage.py migrate
```

run the server

 ```
python3 manage.py runserver

```

