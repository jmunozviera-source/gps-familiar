from fastapi import FastAPI
import sqlite3
from datetime import datetime

app = FastAPI()

@app.post("/update")
async def update_location(data: dict):
    # Sin seguridad por ahora, aceptamos todo
    lat = data.get("lat")
    lon = data.get("lon")
    tid = data.get("tid", "usuario")
    
    conn = sqlite3.connect("ubicaciones.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS locs (tid TEXT, lat REAL, lon REAL, time TEXT)")
    cursor.execute("INSERT INTO locs VALUES (?, ?, ?, ?)", 
                   (tid, lat, lon, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return {"status": "ok"}
