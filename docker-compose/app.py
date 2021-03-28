from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return (f'Hello from Container! I have been seen {redis.get('hits')} times and my hostname is {socket.gethostname()}\n')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)