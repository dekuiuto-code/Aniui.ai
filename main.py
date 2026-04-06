@app.route('/voice_cmd', methods=['GET', 'POST'])
def voice_cmd():
    # 1. Try to get command from URL (for KLWP Web Get)
    # 2. Try to get command from JSON (for Tasker/Assistant)
    command = request.args.get('command') or ""
    if not command and request.is_json:
        command = request.json.get('command', "")

    command = command.lower()

    # Your AI Logic
    if "system on" in command:
        data_store["switches"]["power"] = 1
        data_store["last_voice"] = "System Activated"
    elif "glass mode" in command:
        data_store["ui_style"] = "glass"
        data_store["last_voice"] = "Applying Glassmorphism"

    return jsonify(data_store)
    
