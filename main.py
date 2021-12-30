# coding: utf-8

"""
    SatuData API

    Documentation SatuData API v3.0
"""


from fastapi import FastAPI


from routers.input_data_router import router as InputDataRouter
from routers.input_history_router import router as InputHistoryRouter
from routers.master_data_router import router as MasterDataRouter
from routers.opd_router import router as OPDROuter
from routers.role_router import router as RoleRouter
from routers.satuan_router import router as SatuanRouter
from routers.satuan_type_router import router as SatuanTypeRouter
from routers.urusan_router import router as UrusanRouter
from routers.user_router import router as UserRouter

from db import base_class

app = FastAPI(
    title="SatuData API",
    description="Documentation SatuData API",
    version="3.0",
)

app.include_router(InputDataRouter)
app.include_router(InputHistoryRouter)
app.include_router(MasterDataRouter)
app.include_router(OPDROuter)
app.include_router(RoleRouter)
app.include_router(SatuanRouter)
app.include_router(SatuanTypeRouter)
app.include_router(UrusanRouter)
app.include_router(UserRouter)
