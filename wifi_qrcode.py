import qrcode
import json

def generate_wifi_qr(ssid, password, security="WPA", hidden=False):
    """
    Generate a QR code for WiFi access.
    
    Parameters:
    - ssid: Network name (SSID)
    - password: WiFi password
    - security: Security type (WPA, WEP, or nopass for open networks)
    - hidden: Set to True if the network is hidden
    """

    # Load default settings from JSON file 
    with open('./default.json', 'r') as f:
        settings = json.load(f) 

    ssid = settings.get('ssid', 'default_ssid') 
    password = settings.get('password', 'default_password') 
    security = settings.get('security', 'WPA')  # Default to WPA if not specified
    # security can be "WPA" (default), "nopass" for no password  or "WEP" or "nopass"

    wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

    #img = qrcode.make(wifi_config)
    #img.save("wifi_qr.png")  


    # Create the WiFi configuration string
    # Format: WIFI:T:security_type;S:ssid;P:password;H:hidden;;
    hidden_flag = "true" if hidden else "false"
    

    if ssid == "default_ssid" and password == "default_password":  
        print("Using default settings from 'default.json' file.")
    elif security.upper() == "NOPASS":
        wifi_config = f"WIFI:T:nopass;S:{ssid};H:{hidden_flag};;"
    else:
        wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};H:{hidden_flag};;"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(wifi_config)
    qr.make(fit=True)
    
    # Create an image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    filename = f"wifi_qr_{ssid}.png"
    img.save(filename)
    print(f"QR code saved as '{filename}'")
    print(f"Scan this QR code to connect to: {ssid}")
    
    return img


# Example usage
if __name__ == "__main__":
    # Replace these with your WiFi credentials
    SSID = "YourNetworkName"
    PASSWORD = "YourPassword123"
    SECURITY = "WPA"  # Options: WPA, WEP, or nopass
    
    #generate_wifi_qr(SSID, PASSWORD, SECURITY)
    generate_wifi_qr("","","")
    
    # Example for open network (no password):
    # generate_wifi_qr("OpenNetwork", "", security="nopass")
