from flask import Flask, request
import random, json
import requests
import os

app = Flask(__name__)


# exposing the resource /api for the HTTP POST method
@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':

        # read the request body as json
        # extra validations can be done to check if the content-type is json, send bad request if not

        request_json = request.get_json()
        print(request_json) # for debug purpose

        # should have a check if key 'message' exists or not, send bad request if not
        # call method get_reverse() which invokes /reverse mircoservice
        request_json['message'] = get_reverse(request_json['message'])
        request_json['rand'] = random.random()  # generate a random number each time
        request_json['version'] = 'v1' # for future use
        return request_json, 200


def get_reverse(input_string='spOveD'):
    request_json = dict()
    request_json['message'] = input_string
    print(request_json)

    # prepare the request headers
    headers = {'Content-type': 'application/json'}

    # get microservice URL, if the value is not defined use the default value
    reverse_service = os.getenv('REVERSE_SERVICE', 'http://127.0.0.1:5000')

    print("calling reverse service at : " + reverse_service)

    # make a post request
    response = requests.post(reverse_service + '/reverse', data=json.dumps(request_json), headers=headers)
    response_json = response.json()
    return response_json['message']


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0') # listens on port 5001
