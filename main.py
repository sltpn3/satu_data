# coding: utf-8

"""
    SatuData API

    Documentation SatuData API v3.0
"""


from fastapi import FastAPI

from routers.satuan_type_router import router as SatuanTypeRouter

app = FastAPI(
    title="SatuData API",
    description="Documentation SatuData API",
    version="3.0",
)

app.include_router(SatuanTypeRouter)
