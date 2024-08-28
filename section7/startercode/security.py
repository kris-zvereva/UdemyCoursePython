from hmac import compare_digest
from section7.startercode.models.user import UserModel


def authenticate(username, password):
    """
    function that gets called when a user calls the /auth endpoint
    with their username and password
    :param username: user's username in string format
    :param password: user's un-encrypted password in string format
    :return: a UserModel object if authentication was successful, None otherwise
    """

    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    """
    Function that gets called when user has already authenticated and Flask-JWT
    verified their authorization header is correct.
    :param payload: a dictionary with 'identity' key which is the user id
    :return: a UserModel object
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
