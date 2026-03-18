from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/ask")
def hello_index():
    return {"You": "are a pretty girl)) kitty"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)