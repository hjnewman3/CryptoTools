from fastapi import FastAPI
from routers import GreatestCommonDivisorRouter, InverseRouter

app = FastAPI()
app.include_router(GreatestCommonDivisorRouter.router)
app.include_router(InverseRouter.router)

@app.get("/")
def hello():
  return { 'message: Hello World!' }

