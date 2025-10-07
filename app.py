from flask import Flask
from .api.routes import predict_bp

app = Flask(__name__)
app.register_blueprint(predict_bp)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Housing Price Predictor API!"
