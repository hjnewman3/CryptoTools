from fastapi import FastAPI
from routers import gcd, inverse

app = FastAPI()
app.include_router(gcd.router)
app.include_router(inverse.router)

@app.get("/")
def hello():
  return { 'message: Hello World!' }

