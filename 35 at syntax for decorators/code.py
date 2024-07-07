# this syntax prevents func from being created as is
# and instead it will create it and pass it through the decorator in one go

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())  # No admin permissions for jose.
print(get_admin_password.__name__)  # secure_function

# -- keeping function name and docstring --
import functools

user = {"username": "jose", "access_level": "guest"}


def make_secure(func):  # this is a decorator
    @functools.wraps(func)  # keeps the name and docs for the orig func
    def secure_function():  # this is not a decorator. this is a func that will replace the other one
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)  # get_admin_password

