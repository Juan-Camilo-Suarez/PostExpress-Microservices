from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://your_username:your_password@db/main'
CORS(app)

db = SQLAlchemy(app)


@app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
