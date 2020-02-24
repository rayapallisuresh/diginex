from flask import Flask, escape, request, jsonify
import random
app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse():
  if(request.method == 'POST'):
    # parse the request body json
    request_json = request.get_json()
    print(request_json)

    # get the lngth of the string
    input_string = request_json['message']
    string_length = len(input_string)

    # replace the string with 
    request_json['message'] = input_string[string_length::-1]
    return request_json, 200

if __name__ == '__main__':
  app.run(debug=True, port=5000, host='0.0.0.0')
