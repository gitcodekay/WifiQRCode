# WiFi QR Code Generator

A minimal Python utility to generate Wi-Fi QR codes (PNG).  
This version supports WPA and WPA2.  
Distribution, Docker, authentication, CI/tests, rate limiting, and production improvements will be handled in later iterations.

## Features
- Core library: generate_wifi_qr()
- CLI for local QR generation
- Local Flask API endpoint: POST /generate → PNG
- WPA + WPA2 supported

## Installation
```
pip install -r requirements.txt
```

## Usage

### CLI
```
python cli.py --ssid MyWiFi --password Secret --security WPA2
```

### REST API
```
python app.py
curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json"   -d '{"ssid":"MyWiFi","password":"pass","security":"WPA2"}' --output wifi.png
```

## Notes
- Passwords are not logged.
- Production-level hardening is planned for later iterations.