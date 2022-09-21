import requests
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    abc = 1
    res = {"is_exist": False,
         "is_correct": False}
    if abc == 1:
        res["is_exist"] = True

    yres = json.dumps(res)

    print(request.json)
    return yres


if __name__ == '__main__':
    app.run(debug=True, port=9000)


