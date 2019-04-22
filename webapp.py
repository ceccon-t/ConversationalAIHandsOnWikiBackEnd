from flask import Flask, request, jsonify

import json
import os
import sys
import datetime
from BotRequest import BotRequest
import service

app = Flask(__name__)

running_local = len(sys.argv) > 1 and "local" in sys.argv
port = "5000" if running_local else int(os.environ["PORT"])
host = "127.0.0.1" if running_local else "0.0.0.0"


@app.route('/', methods=['GET'])
def index_get():
    return jsonify(
        status=200,
        message="Up and running"
    )


@app.route('/', methods=['POST'])
def index():
    if running_local:
        data = json.loads(request.get_data())
        with open(os.path.join("logs", "request_payload_" + str(datetime.datetime.now()).replace(".", "-").replace(":", "-").replace(" ", "-") + ".json"), 'w') as f:
            f.write(json.dumps(data))

    return jsonify(
        status=200,
        replies=[{
            'type': 'text',
            'content': "Request received"
        }]
    )


@app.route('/info', methods=['POST'])
def info():
    data = json.loads(request.get_data())
    req = BotRequest(data)
    replies = service.process_info(req)
    return jsonify(
        status=200,
        replies=replies
    )


@app.route('/errors', methods=['POST'])
def errors():
    print(json.loads(request.get_data()))
    return jsonify(status=200)


app.run(port=port, host=host)
