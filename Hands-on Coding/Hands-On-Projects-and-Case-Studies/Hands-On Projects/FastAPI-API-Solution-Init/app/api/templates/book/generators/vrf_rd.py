from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  VrfRds,  BgpDc
VRF_RD_INTERNAL_CLIENT_LOWER_LIMIT = 10000
VRF_RD_INTERNAL_CLIENT_UPPER_LIMIT = 19999
VRF_RD_EXTERNAL_CLIENT_LOWER_LIMIT = 20000
VRF_RD_EXTERNAL_CLIENT_UPPER_LIMIT = 29999
async def generate_vrf_rd(template_vars, network_bus) -> str:

    ## Checking if VRF name already in use
    try:
        vrf_obj = await VrfRds.get(vrf_name=template_vars.vrf_name)
        if vrf_obj:
            raise HTTPException(status_code=400, detail=f"The Vrf name is already in use.")
    except DoesNotExist:
        pass

    ## Getting vrd_rd entry by network bus sorted descending by vrf_id
    vrf_network_bus = await VrfRds.filter(network_bus_id=network_bus.id).order_by('-vrf_id').first()

    # if there is no vrf yet associated with the corresponding network bus so start with the initial range
    if vrf_network_bus is None:
        match network_bus.client_type.client_type.lower():
            case 'interno':
                vrf_id = VRF_RD_INTERNAL_CLIENT_LOWER_LIMIT
            case 'externo':
                vrf_id = VRF_RD_EXTERNAL_CLIENT_LOWER_LIMIT
    else:
        vrf_id = vrf_network_bus.vrf_id + 1

    # check upper limits for vrf-id
    match network_bus.client_type.client_type.lower():
        case 'interno':
            if vrf_id > VRF_RD_INTERNAL_CLIENT_UPPER_LIMIT:
                raise HTTPException(status_code=400, detail=f"The VRF ID value for clients of type 'interno' has reached its limit.")
        case 'externo':
            if vrf_id > VRF_RD_EXTERNAL_CLIENT_UPPER_LIMIT:
                raise HTTPException(status_code=400, detail=f"The VRF ID value for clients of type 'externo' has reached its limit.")

    ## Getting the as bgp dc value associated with the network bus
    try:
        bgp_dc = await BgpDc.get(network_bus_id=network_bus.id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"The associated network bus does not match any bgp dc value.")
    
    vrf_rd = f"{bgp_dc.as_bgp}:{vrf_id}"

    ## Create new vrf rd database entry
    try:
        vrf_rd_obj = await VrfRds.create(vrf_name=template_vars.vrf_name, vrf_rd=vrf_rd, network_bus_id=network_bus.id,
                                          vrf_id=vrf_id)
    except IntegrityError:
        raise HTTPException(status_code=401, detail=f"VRF RD already exists.")

    return vrf_rd_obj

