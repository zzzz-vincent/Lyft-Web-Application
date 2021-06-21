from flask import Flask
from flask_restful import Api

from handler import Handler

app = Flask(__name__)
api = Api(app)

api.add_resource(Handler, '/test')


@app.errorhandler(404)
def handle_404(e):
    # handle all other routes here
    return 'Not Supported, use POST /test'


if __name__ == '__main__':
    app.run(debug=True)
