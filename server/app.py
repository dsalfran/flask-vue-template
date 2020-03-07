"""Flask App"""
# ---------------------------------------------
# System modules
# ---------------------------------------------
import os

# ---------------------------------------------
# External dependencies
# ---------------------------------------------
from flask import Flask, send_from_directory
from flask_cors import CORS

# ---------------------------------------------
# Local dependencies
# ---------------------------------------------
from utils.logger import logger

# ---------------------------------------------

app = Flask(__name__, static_folder="../dist", template_folder="../dist")
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    logger.info("Starting Server")
    app.run(use_reloader=True, port=5000, threaded=True)
    logger.info("App started")
