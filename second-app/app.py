from chalice import Chalice
from hashlib import *
import json
from base58 import b58encode
from base64 import b64encode
from werkzeug.security import generate_password_hash

app = Chalice(app_name='second-app')


@app.route('/strtohash/{strData}')
def index(strData):
    data = strData.encode('utf-8')
    return {'inputMsg':strData, 'md5':md5(data).hexdigest(), 'sha256':sha256(data).hexdigest(), 
            'sha224':sha224(data).hexdigest(),'sha1':sha1(data).hexdigest(), 
            'sha512':sha512(data).hexdigest(), 'base58': b58encode(data).decode('utf-8'), 
            'base64':b64encode(data).decode('utf-8'), 'password_hash':generate_password_hash(strData)}

