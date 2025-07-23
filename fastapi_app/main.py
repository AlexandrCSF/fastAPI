import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from src.authorization.endpoints import router as user_router

app = FastAPI()
app.include_router(user_router)

def custom_openapi():
    openapi_schema = get_openapi(
        title="FastAPI",
        version="1.0.0",
        description="FastAPI test app",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "Bearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Enter your JWT token in the format: **Bearer <token>**",
        }
    }

    for path, methods in openapi_schema["paths"].items():
        for method in methods.values():
            if path == "/token/":
                continue
            method.setdefault("security", [{"Bearer": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
