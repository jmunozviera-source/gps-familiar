from fastapi import FastAPI, Header, HTTPException
import sqlite3
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

# Clave que configuramos
CLAVE = "misuperclave123"

@app.post("/update")
async def update_location(data: dict, x_api_key: str = Header(None)):
    # Validamos la clave (si la envías en la cabecera como 'x-api-key')
    if x_api_key != CLAVE:
        raise HTTPException(status_code=403, detail="Clave incorrecta")
    
    # OwnTracks envía 'lat', 'lon' y 'tid' (tracker ID)
    # Usamos .get para que no falle si algún campo falta
    lat = data.get("lat")
    lon = data.get("lon")
    tid = data.get("tid", "usuario")
    
    # Guardamos en la base de datos
    conn = sqlite3.connect("ubicaciones.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS locs (tid TEXT, lat REAL, lon REAL, time TEXT)")
    cursor.execute("INSERT INTO locs VALUES (?, ?, ?, ?)", 
                   (tid, lat, lon, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    
    return {"status": "ok"}
