from jinja2 import Environment, PackageLoader, select_autoescape, meta
import re 

def get_templates(config, template_path_1,file_name):


    env = Environment(
        loader=PackageLoader("app","templates"),
        autoescape=select_autoescape()
    )
   
    template_1 = env.get_template(template_path_1)
    template_list = { "template1":template_1.render(config),"file_name":file_name}
    
    return template_list