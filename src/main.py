import uvicorn
import compas_nurbs, compas
from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {
        "compas": "version: {0}".format(compas.version),
        "compas_nurbs": "version: {0}".format(compas_nurbs.__version__)
        }