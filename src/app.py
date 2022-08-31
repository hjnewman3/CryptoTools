from fastapi import FastAPI
from src.routers import ExtendedEuclideanRouter, GreatestCommonDivisorRouter, RSARouter, SquareAndMultiplyRouter

app = FastAPI()
app.include_router(GreatestCommonDivisorRouter.router)
app.include_router(ExtendedEuclideanRouter.router)
app.include_router(RSARouter.router)
app.include_router(SquareAndMultiplyRouter.router)
