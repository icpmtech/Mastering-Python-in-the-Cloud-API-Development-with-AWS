from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.database.models import TemplateVars


TemplateVarsInSchema = pydantic_model_creator(
    TemplateVars, name="TemplateVarsIn", exclude=["template_id"], exclude_readonly=True)
TemplateVarsOutSchema = pydantic_model_creator(
    TemplateVars, name="TemplateVars", exclude =["modified_at"]
)

class UpdateTemplateVar(BaseModel):
    variable_name: Optional[str]
    variable_value: Optional[str]