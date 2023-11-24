from fastapi import HTTPException
import re


def validate_ixs(template_vars):
    if not re.match(r'IXS\.\d+\.\d+', template_vars.ixs):
        raise HTTPException(status_code=400, detail=f"IXS value does not have the correct format.")