from fastapi import FastAPI
from pydantic import BaseModel
import uVicorn

app = FastAPI()


class Inputs(BaseModel):
    inp: int
    inpt2: str



@app.get("/exemplo")
def exemplo() -> str:
    return "hello mundo"
    #status_code == 200
    #result = "hello mundo"

@app.post("/exemplo_2")
def exemplo_2(inputs:Inputs) -> str:
    return inputs.inpt2


if __name__ == "__main__":
    uVicorn.run(app, port=8000)