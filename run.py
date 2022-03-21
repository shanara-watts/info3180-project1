#! /usr/bin/env python
from app import app
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True,host="0.0.0.0",port=8080)