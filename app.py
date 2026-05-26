from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
    supports_credentials=True,
)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
