from json import dumps

from flask import Blueprint, current_app, request

from generics.communicator.db import get_commands

api = Blueprint('communicator_api', __name__, static_folder='static')

@api.route('/commands/<string:guid>')
def commands(guid: str):
    redis = current_app.config['REDIS']
    start_at = request.args.get('start_at')

    commands, last_id = get_commands(redis, guid, start_at)
    return dumps({'commands':commands, 'last_id':last_id})