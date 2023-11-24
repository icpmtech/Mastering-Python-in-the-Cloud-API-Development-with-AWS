from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError
from app.database.models import  BgpBbip
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn


async def get_bgp_bbip_config( config ,template_vars: AidcTemplateIn): #-> TemplateVarsOutSchema:

    

    try:
        bgp_bbip = await BgpBbip.filter(external_network=template_vars.external_network)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"External network does not match any know value.")
    if isinstance(bgp_bbip, list):
        config['AS_A_IPv4_BBIP'] = config['AS_B_IPv4_BBIP'] = bgp_bbip[0].as_bbip
    else:
        config['AS_A_IPv4_BBIP'] = config['AS_B_IPv4_BBIP'] = bgp_bbip.as_bbip
    
    return config