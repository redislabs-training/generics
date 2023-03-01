# Redis Streams Communicator

Full stack stream messaging solution.  Takes messages from anywhere via a Redis stream and populates them in html via jquery polling.  Can be tied to an individual session/request by using a unique guid.  Use for seamless async communication.

## Installation
`poetry add git+https://github.com/redislabs-training/generics.git`

## Add Blueprint to Flask
Configure Redis connection

```python
app.config["REDIS_URL"] = os.environ['REDIS_URL']
```
or 
```python
app.config['REDIS'] = Redis.from_url(os.environ['REDIS_URL'])
```
Then register the blueprint

```python
from generics.communicator import communicator_api

app = Flask(__name__)
app.register_blueprint(communicator_api, url_prefix='/api/communicator')
```

## Add hooks to templates

```html
<link rel="stylesheet" type="text/css" href="{{url_for('communicator_api.static', filename='communcator.css')}}">
<script type="text/javascript" src="{{url_for('communicator_api.static', filename='communicator.js')}}"></script>
```

CSS is not required, but does a nice highlight effect.

Add `redis-commands-output` class to container div.

```html
<div class="redis-commands-output"></div>
```

When you want to use it, trigger the polling loop with the following Javascript:
```javascript
pollRedisCommands(GUID, populateRedisCommands(GUID), INTERVAL)
```

The GUID provided must match the one used by the backend services sending the messages.

```python
from generics.communicator import set_or_print_commands
set_or_print_commands(redis_conn, GUID, command, processing_time)
```
