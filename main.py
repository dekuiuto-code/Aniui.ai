@app.route('/voice_cmd', methods=['GET', 'POST'])
def voice_cmd():
    global data_store # Ensure we are modifying the main data object
    
    # 1. Extract the command
    command = request.args.get('command') or ""
    if not command and request.is_json:
        command = request.json.get('command', "")

    command = command.lower().strip()

    # 2. Logic Processing
    if not command:
        data_store["last_voice"] = "Listening..."
    elif "system on" in command:
        data_store["switches"]["power"] = 1
        data_store["last_voice"] = "System Online"
    elif "glass mode" in command:
        data_store["ui_style"] = "glass"
        data_store["last_voice"] = "Glassmorphism Applied"
    else:
        # This helps you debug! It shows what the server actually heard.
        data_store["last_voice"] = f"Unknown: {command}"

    return jsonify(data_store)
    
