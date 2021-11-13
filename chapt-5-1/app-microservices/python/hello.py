
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    dictionary = {'Welcome to Developing Cloud Native Apps on GCP': ''}
    return jsonify(dictionary)

if __name__ == '__main__':
    app.run(debug=True)
