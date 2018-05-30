from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', default = 'world', type = str)
    out = f'Hello, {name}!'
    return out

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
