from datetime import datetime
from app.schemas.aidc_internet_telepac_template import AidcTemplateIn
import app.api.templates.book.loaders.loader_template as loader_template;
from app.api.templates.book.commom.utils import  utils;

from app.api.templates.book.managers.files import file_manager
# These values are always the same for this template


Template1="Template/template_1.txt"


async def generate_template(aidc_template_in: AidcTemplateIn):
    
    manual_vlan_reservation = False

    configDto = {}

   
   
    file_name_flag = "template-id-{}".format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    await file_manager.create_file_template(configDto,file_name_flag)
    template = loader_template.get_templates(configDto,Template1,file_name_flag)
    
    return template
   

   