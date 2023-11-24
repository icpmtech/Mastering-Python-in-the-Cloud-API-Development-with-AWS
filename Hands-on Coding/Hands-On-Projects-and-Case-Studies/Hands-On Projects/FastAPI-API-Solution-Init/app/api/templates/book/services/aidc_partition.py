from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  AidcPartition
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn


async def get_aidc_partition(template_vars: AidcTemplateIn): #-> TemplateVarsOutSchema:

    try:
        aidc_partition = await AidcPartition.get(aidc_partition=template_vars.aidc_partition)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Aidc partition does not match any know value.")
    
    return aidc_partition