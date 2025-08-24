from flask import Flask
from pathlib import Path
from .main import main as main_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "chave-secreta"
    app.config["CSV_PATH"] = str(Path(__file__).resolve().parents[1] / "data" / "dados.csv")
    app.register_blueprint(main_bp)
    return app