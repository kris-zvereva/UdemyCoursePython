"""
BaseTest

This class should be the parent class to each non-unit test.
It allows to instantiation of the database dynamically
and makes sure it is a new, blank database each time.
"""

from unittest import TestCase
from section5.starter_code.app import app
from section5.starter_code.db import db


class BaseTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite:///"

    def setUp(self):
        # db exists
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app.config['SQLALCHEMY_DATABASE_URI'] = BaseTest.SQLALCHEMY_DATABASE_URI
        with app.app_context():  # context manager. as if the app is running
            db.init_app(app)
            db.create_all()
        # get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # db is blank
        with app.app_context():
            db.session.remove()  # remove everything from the current session
            db.drop_all()

