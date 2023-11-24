from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  Vbus,Interfaces
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn


async def get_interfaces(vbus_obj: Vbus):
     
    try:
        interfaces_objs = await Interfaces.filter(vbus_id=vbus_obj.id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"The associated vbus does not match any interfaces value. Interfaces need to be created before assinging a service_id")
    
    if(len(interfaces_objs)==2):
        return interfaces_objs
    else:
        raise HTTPException(status_code=404, detail=f"The interfaces aren't correctly configured for the Vbus in use.")
    

async def update_interface(interface: Interfaces,service_id):

    data_dict={"service_id_id":str(service_id) }

    try:
        await interface.update_from_dict(data_dict)
    except DoesNotExist as e :
        raise HTTPException(status_code=404, detail=f"Error on update the service id to the interface{e}")   