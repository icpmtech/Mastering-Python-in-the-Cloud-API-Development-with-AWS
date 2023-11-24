from fastapi import HTTPException


def validate_shape(template_vars):
    if template_vars.egressshape <= 10:
        return
    elif template_vars.egressshape < 1000 and template_vars.egressshape % 10 == 0:
        return
    elif template_vars.egressshape >= 1000 and template_vars.egressshape % 100 == 0:
        return
    else:
        raise HTTPException(status_code=400, detail=f"The shape value specified is not supported.")