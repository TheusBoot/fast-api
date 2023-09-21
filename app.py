from fastapi import FastAPI

app = FastAPI()


@app.get("/exemplo")
def exemplo() -> str:
    return "hello mundo"
    #status_code == 200
    #result = "hello mundo"



if __name__ == "__main__":
    uVicorn.run(app, port=8000)