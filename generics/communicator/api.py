from json import dumps

from flask import Blueprint, current_app, request
from redis import Redis
from redis.exceptions import ResponseError

from generics.communicator.db import get_commands

api = Blueprint('communicator_api', __name__, static_folder='static')

@api.route('/<string:guid>')
def commands(guid: str):
    start_at = request.args.get('start_at')
    redis = current_app.config.get('REDIS')
    if redis is None:
        redis = Redis.from_url(current_app.config.get('REDIS_URL'), decode_responses=True)
        current_app.config['REDIS'] = redis

    try:
        commands, last_id = get_commands(redis, guid, start_at)
    except ResponseError:
        return dumps({'commands':[], 'last_id':'-'})
    
    return dumps({'commands':commands, 'last_id':last_id})