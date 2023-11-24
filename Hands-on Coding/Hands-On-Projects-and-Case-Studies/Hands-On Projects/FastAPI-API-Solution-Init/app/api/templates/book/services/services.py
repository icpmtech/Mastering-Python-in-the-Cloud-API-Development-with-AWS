from fastapi import HTTPException
from tortoise.exceptions import IntegrityError
from app.database.models import   ServiceIds
from fastapi import HTTPException
from app.database.models import  ServiceIds
SERVICE_TYPE = 9
async def generate_service(client_type):
    
    
    function_type = 50 if client_type.client_type=="interno" else 51
    
    service_ids = await ServiceIds.filter(service_type=SERVICE_TYPE, 
                                                 function_type=function_type).order_by('-sequence_id').first()
    if not service_ids:
        try:
            service_id_obj = await ServiceIds.create(service_type=SERVICE_TYPE,
                                                    function_type=function_type,
                                                    sequence_id=1,
                                                    service_id=int(f"{SERVICE_TYPE}{function_type}1"))
        except IntegrityError as e:
            raise HTTPException(status_code=401, detail=f"Service ID already exists.{e}")
        
    else:
        ## Create new service_id database entry with incrementing sequence value
        sequence = service_ids.sequence_id + 1
        try:
            service_id_obj = await ServiceIds.create(service_type=SERVICE_TYPE,
                                                     function_type=function_type,
                                                     sequence_id=sequence,
                                                     service_id=int(f"{SERVICE_TYPE}{function_type}{sequence}"))
        except IntegrityError as e:
            raise HTTPException(status_code=401, detail=f"Service ID already exists.{e}")
    return service_id_obj