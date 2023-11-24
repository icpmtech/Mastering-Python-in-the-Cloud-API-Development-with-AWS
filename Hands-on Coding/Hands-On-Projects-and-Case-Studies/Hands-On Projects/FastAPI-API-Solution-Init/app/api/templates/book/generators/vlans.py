from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  Vlans
from app.database.enums import FunctionTypeEnum
async def generate_vlans(template_vars, vbus_obj, manual_reservation=False) -> str:

    inner_vlan = 2

    if template_vars.aidc_type == "INTERNET":
        outer_vlan = 230
    else: 
        outer_vlan = 232
        
    ## Getting vlan associated with vbus
    try:
        vlan_obj = await Vlans.filter(vbus_id=vbus_obj.id)
    except DoesNotExist: ## If no vlan yet associated with this vbus then set first value or the manually specified value
        if manual_reservation:
            inner_vlan = template_vars.manual_vlan
        else:
            inner_vlan = 2
    else: ## If there are already vlans present for the vbus, check for existing value and calculate the vlan value
        if manual_reservation:
            try:
                vlan_inner_obj = await Vlans.get(vbus_id=vbus_obj.id, outer_vlan=outer_vlan, inner_vlan=template_vars.manual_vlan)
            except DoesNotExist:
                inner_vlan = template_vars.manual_vlan
            else:
                raise HTTPException(status_code=400, detail=f"The inner vlan value is already in use, for vbus {vbus_obj.vbus} and outer vlan {outer_vlan}.")
        else:
            inner_vlan_obj = await Vlans.filter(vbus_id=vbus_obj.id).order_by('-inner_vlan').first() ##TODO fix the increment
            if inner_vlan_obj is not None: ##TODO Se não existir?
                inner_vlan = inner_vlan_obj.inner_vlan + 1
            else:
                if  inner_vlan > 4094:
                    raise HTTPException(status_code=400, detail=f"The inner vlan value for outer vlan {outer_vlan} has reached its limit.")

    try:
        vlan = await Vlans.create(inner_vlan=inner_vlan, outer_vlan=outer_vlan, vbus_id=vbus_obj.id)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail=f"Creation error in the Vlan:{e}")

    vlan_id = f"{outer_vlan}.{inner_vlan}"
    
    return vlan_id


