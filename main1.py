from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'to jest test'

app.run(port=3000)




























#@app.route('/', methods=['GET'])
#def home_page():
#    deta_set = {'Page': 'Home', 'Message': 'Successfully loaded the home page', 'Timestamp': time.time()}
#    json_dump = json.dumps(data_set)
#
#    return json_dump

