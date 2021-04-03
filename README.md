# To-do-Flask
A ToDo List app built on Flask microframework of Python.
The App performs CRUD operations on sqlite/flask using SQLALCHEMY ORM.

## Installation

Assuming you have Python3 and virtualenv installed.
Else use [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install virtualenv
```
For Linux
```bash
python3 -m venv env

source env/bin/activate
```

For Windows
```bash
python3 -m venv env

.\env\Scripts\activate
```

## Usage

If todo.db file is not present then in python shell

```python
from app import db
db.create_all()
```
In terminal
```bash
python ./app.py
```
