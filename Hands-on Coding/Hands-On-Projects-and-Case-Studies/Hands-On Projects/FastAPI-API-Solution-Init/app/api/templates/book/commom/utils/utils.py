

async def setup_interface_description(aidc_template_in, service_id, _aidctype):
    
    #9000000#IXS.20.99999_PLT-EXEMPLO_FE_100Mbs
    return f"{service_id}#{aidc_template_in.ixs}_{aidc_template_in.plt_cmdb}_{_aidctype.description}_{aidc_template_in.egressshape}Mbps"

async def builder_configDto(aidc_template_in, configDto, vlan_id, vrf_rd_obj):

    configDto['VRFNAME'] = vrf_rd_obj.vrf_name.upper()
    configDto['VRFNAME_LOWCASE'] = vrf_rd_obj.vrf_name.lower()
    configDto['VRFRD'] = vrf_rd_obj.vrf_rd
    configDto['IPPEER_B_IPv4_DC'] = "DUMMY_IP1"

    configDto['IPPEER_A_IPv4_BBIP'] = "DUMMY_IP2"

    configDto['IPPEER_B_IPv4_BBIP'] = "DUMMY_IP3"

    configDto['IPPEER_A_IPv4_DC'] = "DUMMY_IP4"

    configDto['EGRESSSHAPE'] = aidc_template_in.egressshape
    
    configDto['INNERVLAN1'] = configDto['INNERVLAN1'] = vlan_id

    configDto['INNERVLAN2'] = configDto['INNERVLAN2'] = vlan_id

    configDto['SUBINTERFACE1'] = configDto['SUBINTERFACE2'] = vlan_id