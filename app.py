from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

import ipdb; ipdb.set_trace()

# 1. Create a variable pw_hash and set it to the return value of bcrypt.generate_password_hash()
# 2. Use .decode(‘utf-8’) and imspect the difference
# 3. Use bcrypt.check_password_hash(pw_hash, "provided_password")

if __name__ == "__main__":
    app.run(port=4000, debug=True)
