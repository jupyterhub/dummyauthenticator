from jupyterhub.auth import Authenticator

from tornado import gen


class DummyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        return data['username']
