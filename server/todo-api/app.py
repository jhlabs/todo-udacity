from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.todo import Todos
from resources.todo import Todo
from resources.project import Projects
from resources.project import Project
from resources.user import UserRegister
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisextremelysafe'

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    print("Tables created")

jwt = JWT(app, authenticate, identity)

api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/todo/<int:id>')

api.add_resource(Projects, '/projects')
api.add_resource(Project, '/project/<int:id>')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
