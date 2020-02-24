from flask import Flask, request
import random, json
import requests
import os
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
  if(request.method == 'POST'):
    request_json = request.get_json()
    request_json['message'] = get_reverse(request_json['message'])
    request_json['rand'] = random.random()
    return request_json, 200

def get_reverse(input_string='spOveD'):
    request_json = dict()
    request_json['message'] = input_string
    print(request_json) 
    headers = {'Content-type': 'application/json'}
    reverse_service = os.getenv('REVERSE_SERVICE', 'http://127.0.0.1:5000')
    response = requests.post(reverse_service + '/reverse',data=json.dumps(request_json), headers=headers)
    response_json = response.json()
    return response_json['message']
  
if __name__ == '__main__':
  app.run(debug=True, port=8080, host='0.0.0.0')
