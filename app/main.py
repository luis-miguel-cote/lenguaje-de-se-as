from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import numpy as np
from PIL import Image

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Aquí deberías importar tu modelo entrenado
# from tu_modelo import predict_sign

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict/")
async def predict_sign(file: UploadFile = File(...)):
    contents = await file.read()
    foto_mano = np.frombuffer(contents, np.uint8)

    # Procesamiento de imagen: Reemplaza esta sección con la librería que usaremos
    # ejemplo_img = procesar_imagen(nparr)

    # Aquí deberías procesar la imagen y hacer la predicción
    # prediction = predict_sign(ejemplo_img)

    # Por ahora, retornamos un resultado de ejemplo
    prediction = "Ejemplo de seña reconocida"

    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
