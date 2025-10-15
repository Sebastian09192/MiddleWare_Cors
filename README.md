# Proyecto: Middleware CORS en FastAPI

## 📋 Descripción

Este proyecto implementa middleware en FastAPI, incluyendo CORS (Cross-Origin Resource Sharing) y un middleware personalizado para verificar el User-Agent de las peticiones.

## 🎯 Objetivos

- Comprender qué es CORS y por qué es importante
- Implementar middleware CORS en FastAPI
- Mantener middleware personalizado para filtrado de dispositivos móviles
- Documentar el proyecto correctamente

## 🔍 ¿Qué es CORS?

**CORS (Cross-Origin Resource Sharing)** es un mecanismo de seguridad que permite a un servidor especificar qué orígenes (dominios) externos pueden acceder a sus recursos.

### Problema que resuelve

Por defecto, los navegadores web implementan la **Same-Origin Policy** (Política del mismo origen), que bloquea peticiones JavaScript entre diferentes dominios por razones de seguridad.

**Ejemplo:**
- Tu API está en: `http://localhost:8000`
- Tu frontend está en: `http://localhost:3000`
- Sin CORS: ❌ El navegador bloquea las peticiones
- Con CORS: ✅ El servidor permite las peticiones de forma controlada

### Componentes de CORS

1. **Origins permitidos**: Qué dominios pueden acceder
2. **Métodos HTTP**: GET, POST, PUT, DELETE, etc.
3. **Headers**: Qué cabeceras HTTP se permiten
4. **Credentials**: Si se permiten cookies y autenticación

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **FastAPI**: Framework web moderno y rápido
- **Uvicorn**: Servidor ASGI para ejecutar FastAPI

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone [URL-DE-TU-REPOSITORIO]
cd [nombre-del-proyecto]
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install fastapi uvicorn
```

O con archivo requirements.txt:

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## 📚 Endpoints Disponibles

### 1. Endpoint Principal
```
GET /
```
Retorna un mensaje de bienvenida.

### 2. Información del Proyecto
```
GET /info
```
Retorna información sobre los middleware implementados.

### 3. Test de CORS
```
GET /test-cors
```
Endpoint para verificar que CORS está funcionando correctamente.

### 4. Documentación Interactiva
```
GET /docs
```
Swagger UI - Documentación interactiva generada automáticamente.

```
GET /redoc
```
ReDoc - Documentación alternativa.

## 🔧 Configuración de Middleware

### Middleware CORS

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Headers permitidos
)
```

**Nota de Seguridad:** En producción, reemplaza `["*"]` con dominios específicos:

```python
allow_origins=[
    "https://miapp.com",
    "https://www.miapp.com"
]
```

### Middleware Personalizado

El middleware de verificación de User-Agent:
- Intercepta todas las peticiones HTTP
- Verifica si el User-Agent contiene "Mobile"
- Si es móvil: retorna error 401
- Si no es móvil: permite continuar la petición

## 🧪 Pruebas

### Probar sin móvil (Desktop)
```bash
curl http://localhost:8000/
```
**Resultado esperado:** ✅ Respuesta exitosa

### Probar con User-Agent móvil
```bash
curl -H "User-Agent: Mozilla/5.0 (iPhone; Mobile) Safari/537.36" http://localhost:8000/
```
**Resultado esperado:** ❌ Error 401

### Probar CORS desde el navegador

Crea un archivo `test.html`:

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Test CORS</h1>
    <button onclick="testCors()">Probar CORS</button>
    <div id="resultado"></div>

    <script>
        async function testCors() {
            try {
                const response = await fetch('http://localhost:8000/test-cors');
                const data = await response.json();
                document.getElementById('resultado').innerHTML = 
                    'CORS funciona! ' + JSON.stringify(data);
            } catch (error) {
                document.getElementById('resultado').innerHTML = 
                    'Error CORS: ' + error;
            }
        }
    </script>
</body>
</html>
```

Abre este archivo en tu navegador y haz clic en el botón.

## 📁 Estructura del Proyecto

```
proyecto-cors/
│
├── main.py              # Código principal con middleware
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
└── .gitignore          # Archivos a ignorar en Git
```

## 📝 Requisitos del Sistema

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔗 Enlaces Útiles

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de CORS](https://developer.mozilla.org/es/docs/Web/HTTP/CORS)
- [FastAPI CORS Middleware](https://fastapi.tiangolo.com/tutorial/cors/)

## 👨‍💻 Autor

[Tu Nombre]

## 📄 Licencia

Este proyecto es parte de un ejercicio académico.

---

## 🎓 Conceptos Aprendidos

1. ✅ Qué es CORS y por qué es necesario
2. ✅ Cómo implementar middleware en FastAPI
3. ✅ Configuración de CORS para desarrollo y producción
4. ✅ Creación de middleware personalizado
5. ✅ Documentación de proyectos con README.md
6. ✅ Gestión de repositorios Git

## 📌 Notas Adicionales

- El middleware CORS debe añadirse **antes** de otros middleware personalizados para funcionar correctamente
- En producción, siempre especifica orígenes específicos en lugar de usar `"*"`
- El middleware de User-Agent es solo para demostración; en producción considera otros métodos de validación