import json
import traceback

import pandas as pd
from sklearn.externals import joblib
from flask import Flask, request, jsonify, abort
import ssl
from functools import wraps
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('server.crt', 'server.key')

feature_names = joblib.load('feature_names.pkl')
target_names = joblib.load('target_names.pkl')

app = Flask(__name__)
clf = joblib.load('model.pkl')

# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        if request.args.get('key') and request.args.get('key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@app.route('/', methods=['GET'])
@require_appkey
def title_page():
    return 'Iris Rest API'

@app.route('/predict', methods=['POST'])
@require_appkey
def predict():
    try:
        json_ = json.loads(request.json)
        df = pd.DataFrame(json_)[feature_names]
        prediction = clf.predict_proba(df).tolist()
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})

if __name__ == '__main__':
    port = 80
    app.run(host='0.0.0.0', port=port, debug=False)
