from flask import Flask, jsonify
from flask_cors import CORS
import threading
import time

app = Flask(__name__)
CORS(app)

status = {
    "running": False,
    "progress": 0,
    "message": "Idle"
}

@app.route("/")
def home():
    return {"message": "API running"}

@app.route("/status")
def get_status():
    return jsonify(status)

def fake_task():
    status["running"] = True
    status["progress"] = 0
    status["message"] = "Starting..."

    for i in range(101):
        time.sleep(0.05)
        status["progress"] = i
        status["message"] = f"Downloading {i}%"

    status["running"] = False
    status["message"] = "Done"

@app.route("/start")
def start():
    if not status["running"]:
        threading.Thread(target=fake_task).start()
    return {"message": "Started"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)