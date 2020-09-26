from flask_restx import Api
from flask import Blueprint


from .main.controller.user_controller import api as user_ns
from .main.controller.group_controller import api as group_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.logEntry_controller import api as logEntry_ns
from .main.controller.logEntries_controller import api as logEntries_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Simple Operational Logbook',
          version='0.1',
          description='A simple logbook for recording operational activities',
          doc='/api/'
          )


api.add_namespace(group_ns, path='/group')
api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(logEntries_ns, path='/entries')
api.add_namespace(logEntry_ns, path='/entry')
