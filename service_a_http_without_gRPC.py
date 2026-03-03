
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello(name:str):
    print("Service A received:", name)
    return {"message": f"Hello {name} from Service A (HTTP)"}