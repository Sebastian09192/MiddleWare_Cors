from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API con Middleware CORS",
    description="Proyecto que demuestra el uso de middleware personalizado y CORS",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.middleware("http")
async def verifica_agente_usuario(request: Request, call_next):
    """
    Middleware que verifica si la peticion proviene de un dispositivo movil.
    Si es movil, retorna un error 401.
    """
    user_agent = request.headers.get("User-Agent", "")
    
    if "Mobile" in user_agent:
        return JSONResponse(
            content={
                "message": "Error: Acceso desde dispositivo movil no permitido",
                "user_agent": user_agent
            }, 
            status_code=401
        )
    
    response = await call_next(request)
    return response

@app.get("/")
def main():
    """
    Endpoint principal que retorna un saludo.
    """
    return {"message": "Hola! Bienvenido a la API con CORS"}

@app.get("/info")
def info():
    """
    Endpoint de informacion sobre el proyecto.
    """
    return {
        "proyecto": "Middleware CORS en FastAPI",
        "middlewares_implementados": [
            "CORS - Cross-Origin Resource Sharing",
            "Verificación de User-Agent (bloqueo de móviles)"
        ],
        "descripcion": "Este proyecto demuestra el uso de middleware CORS para permitir peticiones cross-origin y un middleware personalizado para filtrar dispositivos moviles."
    }

@app.get("/test-cors")
def test_cors():
    """
    Endpoint para probar que CORS esta funcionando correctamente.
    Puedes llamar a este endpoint desde una página web en otro dominio.
    """
    return {
        "cors_enabled": True,
        "message": "Si puedes ver esto desde otro dominio, CORS está funcionando correctamente"
    }