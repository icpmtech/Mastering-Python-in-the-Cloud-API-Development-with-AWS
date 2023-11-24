from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  Vbus,NetworkBus
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn


async def get_vbus(network_bus: NetworkBus): #-> TemplateVarsOutSchema:
     
    try:
        vbus_obj = await Vbus.get(network_bus_id=network_bus.id, is_active=True)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"The associated network bus does not match any vbus value.")
    
    return vbus_obj