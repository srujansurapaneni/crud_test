# imports
from flask import Flask, request

# define app
app = Flask(__name__)

# define routes and methods
@app.route('/getdata',methods=['GET'])
def get_data():
    return "Getted Data !!"


@app.route('/writedata',methods=['POST'])
def post_data():
    # extract request body
    request_body = request.get_json()
    print(request_body['name'])

    name_str = request_body['name']
    return 'Posted'+name_str


# start server
app.run(port=5000)
