from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
# from werkzeug.security import safe_str_cmp
import secrets
# from werkzeug.security import timing_safe_compare



class User(object):
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password
    
    def __str__(self):
        return "User(id='%s')"%self.id

users = [
    User(1,'user1', 'secret'),
    User(2, 'user2', 'iwonttell')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}
def authenticate(username, password):
    user = username_table.get(username, None)
    # if user and safe_str_cmp(user.password,password):
    if user and secrets.compare_digest(user.password,password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)
@app.route('/protected')
@jwt_required()
def protected():
    return '%s'%current_identity

if __name__ == '__main__':
    app.run