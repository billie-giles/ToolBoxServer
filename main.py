from flask import Flask, request, Response, jsonify
import json
import gpt4all

app = Flask(__name__)

_gpt4all = gpt4all.GPT4All("../models/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
session = _gpt4all.chat_session()


@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})


@app.route('/modellist')
def getBotList():
    return json.dumps(_gpt4all.list_models())


@app.route('/sendmessage', methods=['POST', 'GET'])
def sendMessage():
    msg = str(request.data).replace('\\n', '\n')
    print(msg)
    # with _gpt4all.current_chat_session:
    # with _gpt4all.chat_session():
    # messages_name = [{"role": "user", "content": msg}]

    output = _gpt4all.generate(msg, max_tokens=500)

    print(output)
    x = {
        "message": output
    }

    return json.dumps(x)


app.run()
