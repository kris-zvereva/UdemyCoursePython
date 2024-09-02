from section7.startercode.app import app
from section7.startercode.db import db

# db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
