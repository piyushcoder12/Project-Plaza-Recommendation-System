# user_manager.py

import os
import json

def save_user_history(username, prompt, best_project):
    user_dir = "users"
    os.makedirs(user_dir, exist_ok=True)

    user_file = os.path.join(user_dir, f"{username}.json")

    if os.path.exists(user_file):
        with open(user_file, 'r') as f:
            history = json.load(f)
    else:
        history = []

    history.append({
        "prompt": prompt,
        "best_project": best_project
    })

    with open(user_file, 'w') as f:
        json.dump(history, f, indent=4)

def load_user_history(username):
    user_file = os.path.join("users", f"{username}.json")

    if os.path.exists(user_file):
        with open(user_file, 'r') as f:
            return json.load(f)
    else:
        return []