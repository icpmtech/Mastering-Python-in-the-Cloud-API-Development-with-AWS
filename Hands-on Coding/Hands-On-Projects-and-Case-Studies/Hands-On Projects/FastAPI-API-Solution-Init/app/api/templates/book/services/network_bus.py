from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  NetworkBus,AidcPartition, ClientType

async def get_network_bus( aidc_partition: AidcPartition, client_type: ClientType): 
    
    try:
        network_bus = await NetworkBus.get(aidc_partition_id=aidc_partition.id, client_type_id=client_type.id,is_active=True).prefetch_related('client_type')
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Failed to find the network bus associated with the aidc partition and client type.")
    
    return network_bus