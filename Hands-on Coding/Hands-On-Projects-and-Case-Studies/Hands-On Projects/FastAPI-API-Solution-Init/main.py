from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
import logging

from app.database.register import register_tortoise
from app.database.config import TORTOISE_ORM


Tortoise.init_models(["app.database.models"], "models")

"""
import 'from app.routes import users, notes' must be after 'Tortoise.init_models'
why?
https://stackoverflow.com/questions/65531387/tortoise-orm-for-python-no-returns-relations-of-entities-pyndantic-fastapi
"""
from app.routes import config_templates, aidc_partition, client_type, bgp_bbip, aidc_type, aidc_internet_telepac_template, interfaces


# Setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# Initialize app
app = FastAPI()

# Register middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(config_templates.router)
app.include_router(aidc_partition.router)
app.include_router(client_type.router)
app.include_router(bgp_bbip.router)
app.include_router(aidc_type.router)
app.include_router(interfaces.router)
app.include_router(aidc_internet_telepac_template.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
