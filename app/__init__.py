from flask import Flask
from flask_cors import CORS
from .routes.predict import predict_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    if test_config is not None:
        app.config.update(test_config)

    app.register_blueprint(
        predict_bp
        )

    @app.route("/", methods=["GET"])
    def home():
        return "Welcome to the Housing Price Predictor API!"

    return app
