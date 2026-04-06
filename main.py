from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize your data store globally
data_store = {
    "switches": {"power": 0},
    "ui_style": "default",
    "last_voice": "Waiting for command..."
}

@app.route('/')
def home():
    return "ANI-UI AI Server is Online!"

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/voice_cmd', methods=['GET', 'POST'])
def voice_cmd():
    global data_store
    
    # Get command from URL params or JSON body
    command = request.args.get('command') or ""
    if not command and request.is_json:
        command = request.json.get('command', "")

    command = command.lower().strip()

    if "system on" in command:
        data_store["switches"]["power"] = 1
        data_store["last_voice"] = "System Activated"
    elif "glass mode" in command:
        data_store["ui_style"] = "glass"
        data_store["last_voice"] = "Applying Glassmorphism"
    elif command:
        data_store["last_voice"] = f"Heard: {command}"
    
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
