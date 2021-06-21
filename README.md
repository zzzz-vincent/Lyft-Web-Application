# Demo Web Application

A web application using Flask.

## API

Return a JSON object with the key “return_string” and a string containing every third letter from the original string.
```
POST /test
```

Parameter:

| Name         | Type | In    | Description                        |
| -------------|------|-------| -----------------------------------|
| string_to_cut|string|request| String to be cut every third letter|

Example:

If you post request:
```shell script
$ curl -X POST localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```

the application will return:
```shell script
{
    "return_string": "muydv"
}
```



## Installation

### Virtual environments
Use a virtual environment to manage the dependencies for the project.

Python comes bundled with the `venv` module to create virtual environments

```shell script
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate
```

### Install Flask-RESTful with pip
```python
pip install flask-restful
```

## Running the application
```shell script
$ python app.py
```



