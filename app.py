from flask import Flask, request, send_file, abort
from io import BytesIO
from lib import generate_wifi_qr

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json() or {}

    ssid = data.get("ssid")
    password = data.get("password", "")
    security = data.get("security", "WPA")
    hidden = data.get("hidden", False)

    if not ssid:
        abort(400, description="SSID is required")

    qr_bytes = generate_wifi_qr(ssid, password, security, hidden)

    return send_file(
        BytesIO(qr_bytes),
        mimetype="image/png",
        as_attachment=False,
        download_name="wifi.png"
    )

if __name__ == "__main__":
    app.run(debug=True)
