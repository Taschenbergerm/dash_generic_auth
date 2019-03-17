import base64
import flask
from dash_auth.auth import Auth
from dash_auth import BasicAuth


class GenericAuth(BasicAuth):

    def __init__(self, app, login_func):
        Auth.__init__(self,app)
        self.login_func = login_func

    def is_authorized(self):
        username, password = self.get_user()
        return self.login_func(username, password)

    def get_user(self):
        header = flask.request.headers.get('Authorization', None)
        if not header:
            return (None, None)
        username_password = base64.b64decode(header.split('Basic ')[1])
        username_password_utf8 = username_password.decode('utf-8')
        username, password = username_password_utf8.split(':')
        return (username, password)