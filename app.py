from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', default = 'world', type = str)
    out = f'Hello, {name}!'
    return out

@app.route('/sum')
def sum():
    x = request.args.get('x')
    y = request.args.get('y')
    sum = int(x) + int(y)
    return str(sum)

@app.route('/square')
def square():
    x = request.args.get('x')
    square = int(x) * int(x)
    return str(square)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
