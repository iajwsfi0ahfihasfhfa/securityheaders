import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url", "")
    if not url.startswith("http"):
        return jsonify({"error": "URL must start with http or https"}), 400
    try:
        resp = requests.get(url, timeout=5)
        results = {}
        for header in SECURITY_HEADERS:
            results[header] = resp.headers.get(header)
        return jsonify({"headers": results, "status": "ok"})
    except Exception:
        return jsonify({"error": "Failed to fetch the URL"}), 500

if __name__ == "__main__":
    app.run(debug=True)
