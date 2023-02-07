
# Building A REST API with Flask
A pizza delivery API Built with Flask

## Topics Learned
- How to set up a Flask API with Flask-RESTX
- Databases with FlaskJWT Authentication with Flask-JWT-Extended-SQLAlchemy
- Environment variables with Python-Decouple
- Database migrations with Flask-Migrate
- How to write Unit Tests with Unittest and PyTest
- Documenting REST APIs with SwaggerUI and Flask-RESTX
- Error Handling with Werkzeug

## How to run the project
Clone the project Repository
```$ https://github.com/obaraelijah/REST_API_FLASK.git```

Enter the project folder and create a virtual environment

```$ cd Enter the project folder and create a virtual environment ```

``$ python -m venv env ``

Activate the virtual environment

```
$ source env/bin/actvate #On linux Or Unix

$ source env/Scripts/activate #On Windows 
```

### Install all requirements
``` $ pip install -r requirements.txt```

### Run the project in development
``` 
$ export FLASK_APP=api/

$ export FLASK_DEBUG=1

$ flask run 
```
#### OR
```
python runserver.py
```