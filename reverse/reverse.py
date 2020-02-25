from flask import Flask, escape, request, jsonify
import random

app = Flask(__name__)


@app.route('/reverse', methods=['POST'])
def reverse():
    if request.method == 'POST':
        # parse the request body json
        # read the request body as json
        # extra validations can be done to check if the content-type is json, send bad request if not
        request_json = request.get_json()
        print(request_json)

        # get the length of the string
        # should have a check if key 'message' exists or not, send bad request if not
        input_string = request_json['message']
        string_length = len(input_string)

        # replace the string with
        request_json['message'] = input_string[string_length::-1]
        return request_json, 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') # listens on port 5000
