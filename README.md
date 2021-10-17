# Blog Framework

## 1 - Description
This project is a blog API 

### 2 - Running the application
After cloning this code, you must set up a development environment to run application.
Bellow we have the step by step how to run this application correctly. All commands are related 
to project root.


#### 2.1 Instaling Python dependencies

`python >= 3.8` is required, and it is advisable to create and activate a virtual environment 
named `venv`. In an open terminal, run the command:

```shell
pip install -r requirements.txt
```

#### 2.2 - Create a `.env` file

Copy the content of `local.env` file and then, create a file with name `.env`. Paste the 
copied content to it. You should provide a SQLALCHEMY_DATABASE_URI and if you want a more 
secure SECRET_KEY do the following in a Python shell:

```python
from app.utils.security import generate_secret_key
generate_secret_key(50)
```
Set the generated code as your SECRET_KEY.

#### 2.3 - Migrations

To create the tables on database, run the following command: 

```shell
flask db upgrade
```

#### 2.4 - Run Flask Server

```shell
export FLASK_APP=manage.py
```

```shell
flask run
```
