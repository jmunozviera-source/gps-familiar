from fastapi import FastAPI, Header, HTTPException
import sqlite3
from datetime import datetime

app = FastAPI()

# Clave simple para evitar errores de escritura
CLAVE_SEGURIDAD = "1234"

@app.post("/update")
async def update_location(data: dict, x_api_key: str = Header(None)):
    if x_api_key != CLAVE_SEGURIDAD:
        raise HTTPException(status_code=403, detail="Clave incorrecta")
    
    # ... resto del código para guardar en la base de datos ...
    return {"status": "ok"}
