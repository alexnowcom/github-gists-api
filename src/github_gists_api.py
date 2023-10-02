import requests
import signal
from flask import Flask, jsonify
from markupsafe import escape

app = Flask(__name__)

# GitHub API base URL
GITHUB_API_BASE_URL = "https://api.github.com"

@app.route('/')
def index():
    return jsonify({"error": "Must include username in request"}), 404

@app.route('/<username>')
def get_user_gists(username):
    
    try:
        # Make a request to GitHub API to get the user's public Gists
        response = requests.get(f"{GITHUB_API_BASE_URL}/users/{escape(username)}/gists")
        
        # Check if the request was successful
        if response.status_code == 200:
            gists = response.json()
            return jsonify(gists)
        elif response.status_code == 404:
            return jsonify({"error": "User not found"}), 404
        else:
            return jsonify({"error": "Unable to fetch Gists"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

class GracefulExit:
    exit_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.exit_now = True

if __name__ == '__main__':
    termHandler = GracefulExit()
    while not termHandler.exit_now:
        app.run(debug=True)
