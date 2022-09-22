import requests
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    f = open("User_Data.txt", 'r')
    info = f.read()
    info = info.split()
    res = {"is_exist": False,
         "is_correct": False}
    if request.json.get("login") in info:
        res["is_exist"] = True
        index = info.index(request.json.get("login")) + 1
        usr_password = info[index]
        if request.json.get("haslo") == usr_password:
            res["is_correct"] = True
    yres = json.dumps(res)
    print(request.json)
    return yres



if __name__ == '__main__':
    app.run(debug=True, port=9000)


