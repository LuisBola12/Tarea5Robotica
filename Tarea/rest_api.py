from flask import *
import json, time

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    data_set = {'Page': 'home', 'Message': 'Successfully loaded home page', 'TimeStamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/lesco/',methods=['GET'])
def lesco_page():
    image_query = str(request.args.get('image')) #/lesco/?image=esta va a ser la imagen
    data_set = {'Page': 'Request', 'Message': f'Successfully will convert image to lesco {image_query} ', 'TimeStamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port=8000)
    