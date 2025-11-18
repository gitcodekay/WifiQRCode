from io import BytesIO
import qrcode
import re

def escape_wifi_string(value: str) -> str:
    if value is None:
        return ""
    value = value.replace("\\", "\\\\")
    value = value.replace(";", r"\;")
    value = value.replace(",", r"\,")
    value = value.replace(":", r"\:")
    return value

def build_wifi_payload(ssid: str ="" , password: str = "", security: str = "WPA", hidden: bool = False) -> str:
    ssid_esc = escape_wifi_string(ssid)
    pwd_esc = escape_wifi_string(password)
    sec = (security or "").upper()
    if not sec:
        sec = "nopass"
    payload = f"WIFI:T:{sec};S:{ssid_esc};P:{pwd_esc};"
    if hidden:
        payload += "H:true;"
    payload += ";"
    return payload

def generate_wifi_qr(ssid: str = "", password: str = "", security: str = "WPA", hidden: bool = False) -> bytes:
    payload = build_wifi_payload(ssid, password, security, hidden)
    qr = qrcode.QRCode()
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    bio = BytesIO()
    img.save(bio, format="PNG")
    bio.seek(0)
    return bio.read()
