from cleo import Command
from redis import Redis

class FlushNamespace(Command):
    '''
    Delete all the keys that match the string provided

    flush_namespace
        {namespace : Pattern to delete}
        {--H|redis-host=localhost : Redis Hostname - can also set with REDIS_HOST env var}
        {--P|redis-port=6379 : Redis port - can also set with REDIS_PORT env var}}
    '''

    def handle(self):
        namespace = self.argument('namespace')
        host = self.option('redis-host')
        port = self.option('redis-port')

        r = Redis(host=host, port=port)
        info = r.info('keyspace')
        keys = r.keys(namespace)

        self.line(f'{len(keys)} found! {100 * (len(keys)/info["db0"]["keys"])} % of total keyspace')

        if len(keys) == 0:
            return

        yes = self.confirm('Are you sure you want to delete?')

        if yes: 
            r.delete(*keys)
            

