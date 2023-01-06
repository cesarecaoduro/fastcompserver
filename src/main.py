import uvicorn
import compas_nurbs, compas
from fastapi import FastAPI

PORT = 3000
app = FastAPI(debug=True)

@app.get("/")
def read_root():
    return {
        "compas": "version: {0}".format(compas.version),
        "compas_nurbs": "version: {0}".format(compas_nurbs.__version__)
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)