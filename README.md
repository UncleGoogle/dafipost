# dafipost
Privet-trening app to create and modify short public messages.

https://dafipost.herokuapp.com/

## Development

### Requirements
```
pip install -r requirements_dev.txt
```

### Unit tests
```
pytest
```

### Functional tests

```
python manage.py runserver
pytest --functional
```

### Deployment
```
pip install -r requirements.txt
gunicorn dafipost.wsgi --log-file -
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- then go to admin/socialaccount/socialapp/ and add social integartions
- make sure they are configured properly (redirect_uri) on the other side

#### CD
- Auto deployment enabled for https://dafipost.herokuapp.com/ on push to `main` branch
