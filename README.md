# flask-bcrypt-testing

## [Flask Bcrpyt Usage](https://flask-bcrypt.readthedocs.io/en/1.0.1/#usage)

To use the extension simply import the class wrapper and pass the Flask app object back to here. Do so like this:

```python
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
```

Two primary hashing methods are now exposed by way of the bcrypt object. In Python 2, use them like so:

```python
pw_hash = bcrypt.generate_password_hash('hunter2')
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
```
***In Python 3, you need to use decode(‘utf-8’) on generate_password_hash(), like below:***

```python
pw_hash = bcrypt.generate_password_hash(‘hunter2’).decode(‘utf-8’)
```
