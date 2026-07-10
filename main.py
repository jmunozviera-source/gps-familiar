from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI()

# Definimos una clave que usaremos para que nadie más envíe datos
CLAVE_SEGURIDAD = "misuperclave123"

class LocationUpdate(BaseModel):
    tid: str
    lat: float
    lon: float

@app.post("/update")
async def update_location(data: LocationUpdate, x_api_key: str = Header(None)):
    if x_api_key != CLAVE_SEGURIDAD:
        raise HTTPException(status_code=403, detail="Clave incorrecta")
    
    conn = sqlite3.connect("ubicaciones.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS locs (tid TEXT, lat REAL, lon REAL, time TEXT)")
    cursor.execute("INSERT INTO locs VALUES (?, ?, ?, ?)", 
                   (data.tid, data.lat, data.lon, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return {"status": "ok"}