from fastapi import FastAPI
from producto_router import router
app = FastAPI(
    title="API de Productos :)!!",
    description="API REST para gestionar productos con operaciones CRUD",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/productos",
    tags=["Productos"]
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
