from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

from app.database.models import ConfigTemplates


ConfigTemplateInSchema = pydantic_model_creator(
    ConfigTemplates, name="ConfigTemplateIn", exclude_readonly=True
)
ConfigTemplateOutSchema = pydantic_model_creator(
    ConfigTemplates, name="ConfigTemplateOut", exclude=["created_at", "modified_at", "template"]
)
ConfigTemplateDatabaseSchema = pydantic_model_creator(
    ConfigTemplates, name="ConfigTemplate", exclude=["created_at", "modified_at"]
)

# TODO File serve schema example
# class FileRequestIn(BaseModel):
#     file_id: int
#     file_type: str