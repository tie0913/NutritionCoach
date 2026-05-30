from flask import Flask, g, request
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
    supports_credentials=True,
)

@app.before_request
def load_context():
    g.timezone = request.headers.get(
        "Timezone",
        "UTC"
    )

@app.route('/')
def hello_world():  # put application's code here
    return 'Nutri Coach is Surviving!'


if __name__ == '__main__':
    app.run()
