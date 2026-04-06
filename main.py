from flask import Flask, jsonify, request

app = Flask(__name__)

# This is the memory of your AI
data_store = {
    "switches": {
        "power": 0,      # 0 for Off, 1 for On
        "ui_style": "glass",
        "dev_mode": 1
    },
    "last_voice": "Waiting for command..."
}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "ANI-UI AI Online", "data": data_store})

# Endpoint for KLWP to read data
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

# Endpoint for Voice/Tasker to send instructions
@app.route('/voice_cmd', methods=['POST'])
def voice_cmd():
    incoming = request.json.get("command", "").lower()
    data_store["last_voice"] = incoming
    
    # Simple logic for switches
    if "system on" in incoming:
        data_store["switches"]["power"] = 1
    elif "system off" in incoming:
        data_store["switches"]["power"] = 0
        
    return jsonify({"status": "success", "executed": incoming})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
           
