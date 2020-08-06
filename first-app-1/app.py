from chalice import Chalice
import json

app = Chalice(app_name='first-app')


@app.route('/name/{name}')
def index(name):
    return {'hello': name}


@app.route('/users', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    return json.dumps({'user': user_as_json})
#
# See the README documentation for more examples.
#
