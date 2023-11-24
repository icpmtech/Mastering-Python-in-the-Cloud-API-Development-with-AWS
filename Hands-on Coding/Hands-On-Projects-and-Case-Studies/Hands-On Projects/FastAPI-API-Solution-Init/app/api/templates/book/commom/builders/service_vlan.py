import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.generators.vlans as generator_vlans
import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.services.network_bus as networkbus;
import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.services.v_bus as v_bus;
import app.api.templates.DC_CV_Config_AIDC_L3_INTERNET_MED_template_TELEPAC.services.services as services_service;


async def builder_vlans(aidc_template_in, manual_vlan_reservation, aidcpartition, client_type):
    network_bus = await networkbus.get_network_bus(aidcpartition, client_type)
    vbus_obj = await v_bus.get_vbus(network_bus)
    vlan_id = await generator_vlans.generate_vlans(aidc_template_in, vbus_obj , manual_reservation=manual_vlan_reservation)
    return network_bus,vbus_obj,vlan_id