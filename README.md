# AI DevOps Assistant API

Proyecto de entrenamiento con FastAPI para practicar desarrollo asistido, endpoints REST y validaciones basicas.

## Descripcion General

Esta API expone endpoints simples para:

- verificar que el servicio esta activo,
- obtener una secuencia de Fibonacci,
- consultar informacion del entorno de ejecucion.

Base URL local (por defecto):

- http://127.0.0.1:8000

## Requisitos

- Python 3.9+
- Dependencias en [requirements.txt](requirements.txt)

## Instalacion

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecutar la API

```powershell
uvicorn main:app --reload
```

## Documentacion interactiva

FastAPI genera automaticamente:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

### 1) GET /

Descripcion:

- Endpoint de bienvenida para comprobar conectividad basica.

Respuesta esperada:

```json
{
	"message": "Hello AI DevOps Assistant"
}
```

Ejemplo:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/
```

### 2) GET /fibonacci/{number}

Descripcion:

- Devuelve la secuencia de Fibonacci con la cantidad de elementos indicada por number.
- El calculo comienza en 0, 1.

Parametro de ruta:

- number (int): cantidad de elementos a generar.

Ejemplo:

- Request: GET /fibonacci/6

Respuesta esperada:

```json
{
	"fibonacci_sequence": [0, 1, 1, 2, 3, 5]
}
```

Ejemplo en PowerShell:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/fibonacci/6
```

### 3) GET /system_info

Descripcion:

- Devuelve informacion del entorno del servidor.

Campos devueltos:

- python_version: version de Python en ejecucion.
- current_time: hora actual del servidor en formato ISO.

Respuesta ejemplo:

```json
{
	"python_version": "3.12.2",
	"current_time": "2026-03-12T22:45:10.123456"
}
```

Ejemplo en PowerShell:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/system_info
```

### 4) GET /status

Descripcion:

- Endpoint de health check de la API.
- Actualmente responde con estado y hora del servidor.

Campos devueltos:

- status: mensaje de estado del servicio.
- server_time: hora actual del servidor en formato ISO.

Respuesta ejemplo:

```json
{
	"status": "API running correctly",
	"server_time": "2026-03-12T22:52:29.856621"
}
```

Ejemplo en PowerShell:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/status
```

## Notas tecnicas

- La aplicacion principal esta en [main.py](main.py).
- Existe una doble definicion de la ruta /status en el codigo; esto puede causar confusion de mantenimiento y se recomienda dejar una sola implementacion.

## Dependencias

Ver [requirements.txt](requirements.txt):

- fastapi
- uvicorn
- pytest
