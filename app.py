from flask import Flask, render_template, request, url_for, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('index.html', item=url_for('static', filename='Build/wqe.loader.js'))

@app.route('/data')
def data():
    data = {'message': 'Hello from Flask'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
