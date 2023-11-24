import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.services.interfaces as interfaces_service;
import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.services.services as services_service;
import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.commom.utils.utils as utils;

async def builder_config_services_interface( client_type, vbus_obj,aidc_template_in,_aidctype):
   
   
    interfaces_objs = await interfaces_service.get_interfaces(vbus_obj)
    #atruibir service id to the interface
    config= {}
    service_id=  await services_service.generate_service(client_type)
      #service id to the interface
    await interfaces_service.update_interface(interfaces_objs[0],service_id.id)
    config['INTERFACEDESCRIPTION1'] = await utils.setup_interface_description(aidc_template_in, service_id.service_id, _aidctype)
    service_id_1=  await services_service.generate_service(client_type)
    await interfaces_service.update_interface(interfaces_objs[1],service_id.id)
      #service id to the interface
    config['INTERFACEDESCRIPTION2'] = await utils.setup_interface_description(aidc_template_in, service_id_1.service_id, _aidctype)
    config['INTERFACE1'] = interfaces_objs[0].interface
    config['INTERFACE2'] = interfaces_objs[1].interface
    return config