"""
BaseTest
this should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and make sure that it is a new blank database each time.
"""

from unittest import TestCase
from section5.starter_code.app import app
from section5.starter_code.db import db


class BaseTest(TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

