from fastapi import FastAPI

app = FastAPI()

@app.get("/cachetada")
def read_comestibles():
    return {
        "truchas": [
            'Trucha arcoiris',
            'Trucha de lago',
            'Trucha degollada',
            'Trucha marrón'
        ]
    }