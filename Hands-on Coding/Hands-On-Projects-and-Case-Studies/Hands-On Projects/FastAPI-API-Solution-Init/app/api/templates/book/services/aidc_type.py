from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  AidcType
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn


async def get_aidc_type(template_vars: AidcTemplateIn): #-> TemplateVarsOutSchema:
     
    try:
        aidc_type = await AidcType.get(aidc_type=template_vars.aidc_type)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Aidc type (segment type) does not match any know value.")
    return aidc_type