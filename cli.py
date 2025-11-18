import argparse
import json
from datetime import datetime
from lib import generate_wifi_qr

def load_defaults():
    try:
        with open("default.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    defaults = load_defaults()

    parser = argparse.ArgumentParser(description="Generate WiFi QR codes")
    parser.add_argument("--ssid")
    parser.add_argument("--password")
    parser.add_argument("--security")
    parser.add_argument("--hidden", action="store_true")

    args = parser.parse_args()

    ssid = args.ssid or defaults.get("ssid")
    password = args.password or defaults.get("password", "")
    security = args.security or defaults.get("security", "WPA")
    hidden = args.hidden or defaults.get("hidden", False)

    if not ssid:
        raise SystemExit("SSID is required")

    png_bytes = generate_wifi_qr(ssid, password, security, hidden)
    filename = f"wifi_{ssid}_{datetime.now().strftime('%Y%m%d-%H%M%S')}.png"

    with open(filename, "wb") as f:
        f.write(png_bytes)

    print(f"Saved to {filename}")

if __name__ == "__main__":
    main()
