from json import dumps

from redis import Redis

_key_commands    = lambda guid: f'commands:{guid}'

def get_commands(redis: Redis, guid: str, start_at=None) -> tuple:
    data = redis.xrange(_key_commands(guid), f'({start_at}' if start_at else '-', '+')
    
    if data:
        last_id = data[-1][0]
    else:
        last_id = start_at

    return [record[1] for record in data], last_id

def set_or_print_commands(redis: Redis, guid: str, command: str, time=0):
    if guid is not None:
        if type(command) is not str:
            command = dumps(command)
        redis.xadd(_key_commands(guid), {'command':command, 'time':time})
    else:
        print(command)