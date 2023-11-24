from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  ClientType
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn


async def get_client_type(template_vars: AidcTemplateIn):
    try:
        client_type = await ClientType.get(client_type=template_vars.client_type)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Client type does not match any know value.")
    
    return client_type