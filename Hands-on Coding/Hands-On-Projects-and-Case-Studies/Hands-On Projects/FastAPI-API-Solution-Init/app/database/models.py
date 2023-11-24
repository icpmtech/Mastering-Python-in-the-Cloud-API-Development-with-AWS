from tortoise import fields, models





class ConfigTemplates(models.Model, TimestampMixin):
    id = fields.IntField(pk=True)
    path = fields.CharField(max_length=256)
    name = fields.CharField(max_length=128, unique=True)


class TemplateVars(models.Model, TimestampMixin):
    id = fields.IntField(pk=True)
    template_id = fields.ForeignKeyField(
        "models.ConfigTemplates", related_name="template"
    )
    variable_name = fields.CharField(max_length=64)
    variable_value = fields.JSONField(default=[])




class TemplateFiles(models.Model, TimestampMixin):
    id = fields.IntField(pk=True)
    file_id_timestap = fields.CharField(max_length=128)
    file_name = fields.CharField(max_length=1024)
    file_content = fields.CharField(max_length=5000)

class Books(models.Model, TimestampMixin):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=128)
    content = fields.CharField(max_length=1024)
    file_name = fields.CharField(max_length=5000)

class Authors(models.Model, TimestampMixin):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    books = fields.CharField(max_length=1024)