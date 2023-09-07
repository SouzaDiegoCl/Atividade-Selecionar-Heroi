from flask import Flask
from controllers import routes
import os

app = Flask(__name__, template_folder="views",
            static_folder="static", static_url_path="/static")
routes.init_app(app)
basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    app.run(debug=True)
