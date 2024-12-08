from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime

app = FastAPI()

# Bağlı istemciler için veri yapısı
clients: Dict[str, Dict] = {}

# Komut modeli
class Command(BaseModel):
    client_id: str
    command: str

# Kayıt olan istemciler
@app.post("/register/")
async def register_client(client_id: str):
    if client_id not in clients:
        clients[client_id] = {
            "status": "online",
            "last_response": None,
            "last_seen": datetime.utcnow(),
            "command": None
        }
    return {"status": "registered", "client_id": client_id}

# Komut gönderme
@app.post("/command/")
async def send_command(cmd: Command):
    client = clients.get(cmd.client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    client["command"] = cmd.command
    client["last_seen"] = datetime.utcnow()  # Son görülme zamanını güncelle
    return {"status": "command sent", "command": cmd.command}

# İstemci durumunu sorgulama
@app.get("/clients/")
async def get_clients():
    return clients

# İstemci yanıt gönderme
@app.post("/response/")
async def receive_response(client_id: str, response: str):
    client = clients.get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    client["last_response"] = response
    client["last_seen"] = datetime.utcnow()
    return {"status": "response received", "response": response}
