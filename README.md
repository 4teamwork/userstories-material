# userstory-material

## Development

### Setup

A few steps are needed to setup the viewflow demo.
Run these steps within the project folder.

1. Clone the repository:
```
git clone git@github.com:4teamwork/userstories-material.git
```

2. Change to repository
```
cd userstories-material
```

3. Create and activate a python virtual environment:
```
python3 -m venv . && source bin/activate
```

4. Install the requirements:
```
pip install -r requirements-dev.txt
```

5. Run the migrations:
```
./manage.py migrate
```

6. Create a super user:
```
./manage.py createsuperuser
```

Finally start the django server and navigate to http://localhost:8000/

```bash
./manage.py runserver
```
