from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load commands
def load_commands():
    with open("commands.json") as f:
        return json.load(f)["commands"]

# Load trusted devices
def load_devices():
    with open("trusted-devices.json") as f:
        return json.load(f)["trustedDevices"]

@app.route("/getCommands", methods=["POST"])
def get_commands():
    commands = [{"title": c["title"], "id": c.get("id", "N/A")} for c in load_commands()]
    return jsonify({"status": 1, "message": "Data Fetched Successfully", "payload": [{"commands": commands}]}), 200

@app.route("/runCommand", methods=["POST"])
def run_command():
    data = request.get_json()
    command_id = data.get("commandId")
    commands = load_commands()
    for cmd in commands:
        if cmd.get("id") == command_id:
            # Mock execution for demo purposes
            return jsonify({"status": 1, "message": "Command executed", "payload": [{"result": f"Executed: {cmd['command']}"}]})
    return jsonify({"status": 0, "message": "Command not found"}), 404

if __name__ == "__main__":
    app.run(port=8080, debug=True)
