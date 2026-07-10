from fastapi import FastAPI
import sqlite3
from datetime import datetime

app = FastAPI()

@app.get("/update")
async def update_location(tid: str, lat: float, lon: float):
    # Esto recibe los datos directamente de la URL (ej: /update?tid=Juan&lat=...&lon=...)
    conn = sqlite3.connect("ubicaciones.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS locs (tid TEXT, lat REAL, lon REAL, time TEXT)")
    cursor.execute("INSERT INTO locs VALUES (?, ?, ?, ?)", 
                   (tid, lat, lon, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return {"status": "ok"}