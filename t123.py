from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a list of allowed API keys
allowed_api_keys = ["your_api_key_here"]

# Decorator to verify API key
def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-Key")
        if api_key in allowed_api_keys:
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized"}), 401
    return wrapper

# Protected endpoint
@app.route("/protected", methods=["GET"])
@require_api_key
def protected():
    return jsonify({"message": "Access granted"})

if __name__ == "__main__":
    app.run(debug=True)
