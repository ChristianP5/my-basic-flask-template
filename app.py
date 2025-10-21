from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getRoot():
    return {
        "status": "success",
        "message": "Welcome to the Root!",
        "data": []
    }

app.run(host='0.0.0.0', port=80)