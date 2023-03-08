from uuid import uuid4

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def index(path='/'):
    return jsonify({'path': path, 'guid': str(uuid4())})

def main():
    app.run()
    
if __name__ == '__main__':
    main()