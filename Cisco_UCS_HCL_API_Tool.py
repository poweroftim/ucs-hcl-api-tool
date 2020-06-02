#!/usr/bin/python
import requests
import json
from ucsmsdk.ucshandle import UcsHandle
from collections import OrderedDict
import pandas as pd
import re
from collections import defaultdict
from itertools import chain
from tqdm import tqdm
from clint.textui import colored, puts
import requests_cache

'''
Useful package for exploring objects

from ucsmsdk.ucscoreutils import get_meta_info

Example:
class_meta = get_meta_info("FabricVlan")
print (class_meta)

'''

requests_cache.install_cache(cache_name='hcl_api_cache_db', backend='sqlite', expire_after=180)

######### MAIN MENU
def hcl():
#
    def begin():
        image = ('''











             ..*###(#(#####(##(#(#(#%%(#(#(###(####(#(#%%##%%%%%%%%%%%%%%%%%%%%#%*...       ..*###(###(###(##(#(#(#%%(#(#####(##(#(#(#%%##%%%%%%%%%%%%%%%%%%%%#%/...   
             ..*###//////(///(//////#&//////(///(//////##%%%%%%%%%%%%%%%%%%%%#%*...       ..*###//(///(///(//////#&////(/(///(//////##%%%%%%%%%%%%%%%%%%%%#%/...   
             ..*(%#&&&&&&&&&&&&&&&&&%#&&&&&&&&&&&&&&&&&%#######################(%*. .       ..*(%#&&&&&&&&&&&&&&&&&%#&&&&&&&&&&&&&&&&&%########################%*. .   
                          &*,(                                                                                                                 *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                                  C I S C O   U C S   H C L   A P I   T O O L                                    *( @                    
                          &*,(                                  -------------------------------------------                                    *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                        ..,,, .                          ,,., ,                                                  *( @                    
                          &*,(                                                                                                                 *( @                    
                          &*,(                    ...,.,***,,.,,,.*/.....,.,,,.*/*.....*,**,*.,,,.,/*.....,.,,../*.....*...                    *( @                    
                          &*,(                    ...,..//(#*##%%#((#%##%*#%#%%(((%%%%(**(((#/%%#%(((%%%#(*#%%%#((#%%%#*...                    *( @                    
                          &*,(                    ...*,.//((*#####(##%##%*###%#(#(###%(*.#((#/#%#%(#(%###(/######(#####*..,                    *( @                    
                          &*,@&&&&&&&&&&&&&&&&&&&&%..,..&&/(*#####(##%###*###%#(#(####(*(#//#/####(#(%###(*######(#####*..(&&&&&&&&&&&&&&&&&&&&@/ @                    
                          &(***********************../,.&&/#*##%%#(#####%*#%#%#(#(#%#%(*(#/(#/####(#(####(*######(#%#%#*..************************@                    
                                                  ...,..&&/#*#####(##%###*###%#(#(###%(*(#/(#/####(#(%#%#(/###%##(#####*...                                            
                                                  ...,..&&/#*#####(##%###*#####(#(###%(*(#/(#/%%##(#(%#%#//#%#%##(#%###*...                                            
                                                  /..,..**/#*,,*,,,,*,,,,,,,,,*,,,,,,,,*./,(#,,,,*,,,,,,,,,,,,,,,,,,,,,,.,*.                                           
                                                  ...,..%&/#,.,,,.//.....,.,*,.*/*.....*,&//#.,,*.*//.....,.,*..//.....*...                                            
                                                  ...,..#&/#*#####((#####*(####(((####/*,#/##/####(((####/*#####((#####*..,                                            
                                                  ...,..#&/(*#####(##%##%*###%%(#(###%(**#//#/#%##(#(%###/*#%#%##(#####*..,                                            
                                                  ...,..#&.**#####(##%###*#%##%(#(%##%(**#*,#/####(#(%###//###%##(#%###*..,                                            
                                                  .,.,...,((*###%#(######*##%%#(#(#%#%(*../#(/%#%#(#(#%##//#%####(#%#%#*.,,                                            
                                                  ...,...,/(*#####(##%###*#####(#(#%##(*..//#/####(#(%###//######(#####*...                                            
                                                  ...,....*,*#####(##%##%*#%###(#(###%(*..,,,/###%(#(%#%#//#%####(##%##*...                                            
                                                     ...*,*..,,,,,,,,((,,,*,,,,*,,,,*,,......,,,,*,,,/(/,,,*,,,,*,,.,*,,                                               
                                                      *#////////////%,,(/////////////////////////////#.(/////////////(,                                                
                                                      */((((%%@@@@%%(((((((&%@@@@%%%((((((%%%@@@@%&((((((#%%@@@@%%(((,,                                                
                                                      */((((%%@@@@%%(((((((&%@@@@%%%((((((%%%@@@@%&((((((#%%@@@@%%/((,.                                                
                                                      *(*************************************************************/.    
        








        ''')
        puts(colored.cyan(image))
        #
        #
        #
        print('Press Enter To Begin.')
        begin = input('')
        if begin == '':
            ipAddress()
#
    def ipAddress():
        #
        #
        #
        print('1. Enter IP address of UCSM to query.')
        global ip_address
        ip_address = input('IP Address: ')
        #ip_address = '192.168.1.214'
        if not re.match(r'[0-9]+(?:\.[0-9]+){3}', ip_address):
            print('Invalid IP Address')
        else:
            puts(colored.cyan('Your IP address is ' + ip_address + '\n\n\n'))
            userName()
    #
    def userName():
        print('2. Enter admin username (Local only, please. Default is "admin".)')
        global user_name
        # user_name = 'ucspe'
        user_name = input('Admin username: ')
        puts(colored.cyan('Admin username entered...'))
        print('\n\n\n')
        passWord()
    #
    def passWord():
        print('3. Enter admin password.')
        global pass_word
        pass_word = input('Admin password: ')
        # pass_word = 'ucspe'
        puts(colored.cyan('Admin password entered...\n\n\n'))
        print('\n\n\n')
        loginTest()
    #
    def loginTest():
        global handle
        handle = UcsHandle(ip_address, user_name, pass_word)
        try:
            if handle.login() == True:
                puts(colored.cyan('#####################################################\nUCS Manager Login Successful to ' + ip_address + '\n#####################################################\n\n\n\n'))
            launchQuery()
        except urllib2.URLError:
            puts(colored.red('LOGIN FAILED: Bad IP Address. Please Try Again.'))
            print('\n\n\n')
            ipAddress()
    #
    #----------------------------------------------------------------
    #    LAUNCH APPLICATION
    #----------------------------------------------------------------
    #
    def launchQuery():
        print('Getting Blade Servers from UCS Domain...\n\n')
        getUCSMBlades()
    #
    def getUCSMBlades():
        ###############################
        # BLADE MODEL DICT
        ###############################
        print('\nGetting Blades...\n')
        blade_models_dict = []
        for blade in tqdm(handle.query_classid(class_id="ComputeBlade")):
            blade_models_dict.append((blade.dn, [blade.model]))
            #
        d_models = defaultdict(list)
        for k, v in blade_models_dict:
            d_models[k].append(v)
            #
        sorted(d_models.items())
        d_models = dict(d_models)
        blade_models_dict = d_models
        ###############################
        # BLADE CPUS
        ###############################
        print('\nGetting CPUs...\n')
        blade_cpus_dict = []
        for blade in tqdm(handle.query_classid(class_id="ComputeBlade")):
            for cpu in handle.query_classid(class_id="ProcessorUnit"):
                if blade.dn in cpu.dn:
                    blade_cpus_dict.append((blade.dn, [cpu.rn, cpu.model]))
        #
        d_cpu = defaultdict(list)
        for k, v in blade_cpus_dict:
            d_cpu[k].append(v)
        #
        sorted(d_cpu.items())
        d_cpu = dict(d_cpu)
        blade_cpus_dict = d_cpu
        ###############################
        # BLADE ADAPTERS
        ###############################
        print('\nGetting Adapters...\n')
        blade_adapters_dict = []
        for chassis in tqdm(handle.query_classid(class_id="EquipmentChassis")):
            for chassis_child in handle.query_children(in_mo=chassis):
                if chassis_child.get_class_id() == 'ComputeBlade':
                    for adapt_part in handle.query_children(in_mo=chassis_child):
                        if adapt_part.get_class_id() == 'AdaptorUnit':
                            for blade_part in handle.query_children(in_mo=chassis_child):
                                if blade_part.get_class_id() == 'BiosUnit':
                                    for bios_part in handle.query_children(in_mo=blade_part):
                                        if bios_part.get_class_id() == 'FirmwareRunning':
                                            blade_adapters_dict.append((chassis_child.dn, [adapt_part.model, bios_part.version]))
        #
        d = defaultdict(list)
        for k, v in blade_adapters_dict:
            d[k].append(v)
        #
        sorted(d.items())
        d = dict(d)
        blade_adapters_dict = d
        #
        ###############################
        # MERGE DICTIONARIES
        ###############################
        global blade_attr_dict
        blade_attr_dict = defaultdict(list)
        blade_attr_list = []
        blade_attr_demo = []
        for k, v in chain(blade_adapters_dict.items(), blade_models_dict.items(), blade_cpus_dict.items()):
            blade_attr_dict[k].append(v)
        #
        #pprint.pprint(blade_attr_dict)
        #
        for k, v in blade_attr_dict.items():
            blade_attr_list.append((k, [v]))
        #
        d_attr = defaultdict(list)
        for k, v in blade_attr_list:
            d_attr[k].append(v)
        #
        sorted(d_attr.items())
        d_attr = dict(d_attr)
        blade_attr_dict = d_attr
        #
        ###############################
        # CREATE MODEL LIST
        ###############################
        global blade_model_ucsm_list
        blade_model_ucsm_list = []
        for bl in blade_attr_dict:
            for model in blade_attr_dict[bl]:
                # print bl, model[0][1][0][0][6:9], model[0][1][0][0][10:12]
                blade_model_ucsm = model[0][1][0][0][6:9]
                blade_gen_ucsm = model[0][1][0][0][10:12]
                if blade_model_ucsm not in blade_model_ucsm_list:
                    blade_model_ucsm_list.append([bl, 'B' + blade_model_ucsm + " " + blade_gen_ucsm])
        #
        global blade_models_only_ucsm_list
        blade_models_only_ucsm_list = [item[1] for item in blade_model_ucsm_list]
        # print(blade_models_only_ucsm_list)
        ###############################
        # CREATE BLADE SLOT / MODEL / CPU VERSION LIST
        ###############################
        global v2_xeon
        v2_xeon = '2nd Gen Intel Xeon Processor Scalable Family'
        global v1_xeon
        v1_xeon = 'Intel Xeon Processor Scalable Family'    
        global blade_cpu_versions
        blade_cpu_versions = []
        for bl in blade_attr_dict:
            for blade in blade_attr_dict[bl]:
                blade_model_ucsm = blade[0][1][0][0][6:9]
                blade_gen_ucsm = blade[0][1][0][0][10:12]
                ver = blade[0][2][0][1]
                if "E" in ver[21:27]:
                    global e_cpus
                    e_cpus = ver[21:26] + '00 ' + ver[29:31]
                    blade_cpu_versions.append([bl, 'B' + blade_model_ucsm + " " + blade_gen_ucsm, e_cpus])
                elif "I" in ver[21:29]:
                    blade_cpu_versions.append([bl, 'B' + blade_model_ucsm + " " + blade_gen_ucsm, v2_xeon])
                elif "1" in ver[21:29]:
                    blade_cpu_versions.append([bl, 'B' + blade_model_ucsm + " " + blade_gen_ucsm, v1_xeon])
        launchHCLQuery()
    #
    def launchHCLQuery():
        print('\n\nConnecting to Cisco UCS Hardware Compatibility List API...\n')
        global    hcl_root
        hcl_root = "https://ucshcltool.cloudapps.cisco.com/public/rest/"
        global loadServerTypes
        loadServerTypes = "server/loadServerTypes"
        resp = requests.post(hcl_root + loadServerTypes)
        serverTypes = resp.json()
        # bfw['BladeModel'].unique()
        # global unique_blades
        # unique_blades = bfw['BladeModel'].unique()
        global ub
        ub = []
        # for i in unique_blades:
        #     s = re.split(r'[\s-]+', i)
        #     # print s[1], s[2]
        #     for b in s[1]:
        #         blade_type = s[1][0]
        for t in serverTypes:
            if t['TYPE'] == 'B':
                global bladeRelease
                bladeRelease = t
                # print bladeRelease
                if "UCSM" in bladeRelease['MANAGED']:
                    # print bladeRelease
                    if bladeRelease not in ub:
                        ub.append(bladeRelease)
            #print ub
        vmwareVersion()
    #
    def vmwareVersion():
        print('\n\nRetrieving compatible VMware ESXi versions from CISCO UCS HCL API now...\n\n\n\n\n')
        for u in ub:
            release = u
            if 'B' == release['TYPE']:
                TypeTreeId = {'treeIdRelease' : str(release['T_ID'])}
                loadServerModels = "server/loadServerModels"
                resp = requests.post(hcl_root + loadServerModels, data=TypeTreeId)
                serverModels = resp.json()
                for s in blade_cpu_versions: # blade_models_only_ucsm_list is a list of UCSM blades above.
                    for b in serverModels:
                        if s[1] in b['SERVER_MODEL']:
                            # print b['SERVER_MODEL']
                            # lookup server ID for processors in each server
                            sModelTreeId = {'treeIdServerModel' : b['T_ID']}
                            loadProcessors = "server/loadProcessors"
                            resp = requests.post(hcl_root + loadProcessors, data=sModelTreeId)
                            serverProc = resp.json()
                            # print s[0], s[1]
                            for proc in serverProc:
                                if s[2] == proc['PROCESSOR']:
                                    # print vers['PROCESSOR'], vers['T_ID']
                                    pModelTreeId = {'treeIdProcessor' : proc['T_ID']}
                                    loadOsVendors = 'server/loadOsVendors'
                                    resp = requests.post(hcl_root + loadOsVendors, data=pModelTreeId)
                                    os_list = resp.json()
                                elif s[2] == proc['PROCESSOR'][11:21]:
                                    pModelTreeId = {'treeIdProcessor' : proc['T_ID']}
                                    loadOsVendors = 'server/loadOsVendors'
                                    resp = requests.post(hcl_root + loadOsVendors, data=pModelTreeId)
                                    os_list = resp.json()
                                    #
                            for o in os_list:
                                if 'VMware' in o['OSVENDOR']:
                                    vmware_os = o
                            # lookup OS version for VMware OS
                                    osVendorTreeId = {'treeIdVendor' : vmware_os['T_ID']}
                                    loadOsVersions = 'server/loadOsVersions'
                                    resp = requests.post(hcl_root + loadOsVersions, data=osVendorTreeId)
                                    #
                                    global os_version
                                    os_version = resp.json()
                                    break
        os_version_printed = []
        for v in os_version:
            if v not in os_version_printed:
                os_version_printed.append(v['OSVERSION'])
        s_os_version_printed = sorted(os_version_printed)
        puts(colored.cyan('Available VMware ESXi versions:'))
        for s in s_os_version_printed:
            print('\t' + s)
                                    #
        print('\n\n\n\nEnter VMware ESXi version as displayed above.')
        global vmware_version
        vmware_version = input('VMware ESXi version: ')
        puts(colored.cyan('VMware ESXi version entered...' + vmware_version))
        print('\n\n')
        fullQuery()
        #
    def fullQuery():
        result_cleaned = []
        res = []
        model_list_all = []
        result_list_combined = []
        adapter_firmware_list = []
        all_list = []
        #
        puts(colored.cyan('\n\nRetrieving results...'))
        for u in ub:
            release = u
            if 'B' == release['TYPE']:
                TypeTreeId = {'treeIdRelease' : str(release['T_ID']) }
                loadServerModels = "server/loadServerModels"
                resp = requests.post(hcl_root + loadServerModels, data=TypeTreeId)
                serverModels = resp.json()
                for s in tqdm(blade_cpu_versions): # blade_models_only_ucsm_list is a list of UCSM blades above.
                    for b in serverModels:
                        if s[1] in b['SERVER_MODEL']:
                            # print b['SERVER_MODEL']
                            # lookup server ID for processors in each server
                            sModelTreeId = {'treeIdServerModel' : b['T_ID']}
                            loadProcessors = "server/loadProcessors"
                            resp = requests.post(hcl_root + loadProcessors, data=sModelTreeId)
                            serverProc = resp.json()
                            # print s[0], s[1]
                            for proc in serverProc:
                                if s[2] == proc['PROCESSOR']:
                                    # print vers['PROCESSOR'], vers['T_ID']
                                    pModelTreeId = {'treeIdProcessor' : proc['T_ID']}
                                    loadOsVendors = 'server/loadOsVendors'
                                    resp = requests.post(hcl_root + loadOsVendors, data=pModelTreeId)
                                    os_list = resp.json()
                                elif s[2] == proc['PROCESSOR'][11:21]:
                                    pModelTreeId = {'treeIdProcessor' : proc['T_ID']}
                                    loadOsVendors = 'server/loadOsVendors'
                                    resp = requests.post(hcl_root + loadOsVendors, data=pModelTreeId)
                                    os_list = resp.json()
                                    #
                            for o in os_list:
                                if 'VMware' in o['OSVENDOR']:
                                    vmware_os = o
                            # lookup OS version for VMware OS
                                    osVendorTreeId = {'treeIdVendor' : vmware_os['T_ID']}
                                    loadOsVersions = 'server/loadOsVersions'
                                    resp = requests.post(hcl_root + loadOsVersions, data=osVendorTreeId)
                                    #
                                    global os_version
                                    os_version = resp.json()
                                    for os_vers in os_version:
                                        # print v['OSVERSION']
                                    #
                                        if vmware_version in os_vers['OSVERSION']:
                                            # print b['SERVER_MODEL'], os_vers
                                                query = {'serverType_ID' : str(release['ID']),
                                                  'serverModel_ID' : b['ID'],
                                                  'processor_ID' : proc['ID'],
                                                  'osVendor_ID' : vmware_os['ID'],
                                                  'osVersion_ID' : os_vers['ID'],
                                                  'firmwareVersion_ID' : str(-1),
                                                  'manageType' : release['MANAGED'].strip() }
                                        # print s[1], query
                                                loadSearchResults = 'server/loadSearchResults'
                                                resp = requests.post(hcl_root + loadSearchResults, data=query)
                                                global api_response
                                                api_response = resp.json()
                                                for result in api_response:
                                                    models = (b['SERVER_MODEL'])
                                                    versions = (result['Version'])
                                                    procs = (proc['PROCESSOR'])
                                                    vmware_oss = (vmware_os['OSVENDOR'])
                                                    osversion = (os_vers['OSVERSION'])
                                                    for r in resp.json():
                                                        for attr in r['HardwareTypes']['Adapters']['CNA']:
                                                            adapter_driver = attr['DriverVersion']
                                                            adapter_firmware = attr['FirmwareVersion']
                                                            adapter_pid = attr['Pid']
                                                            adapter_model = attr['Model']
                                                            if result not in all_list:
                                                                all_list.append((models, versions, procs, vmware_oss, osversion, adapter_pid, adapter_model, adapter_firmware, adapter_driver))
                                                                global all_list_pd
                                                                all_list_pd = pd.DataFrame(all_list)
                                #
        all_list_pd.columns =['BladeModels', 'BladeFirmware', 'BladeProcessor', 'BladeOS', 'BladeOSVersion', 'AdapterPid', 'AdapterModel', 'AdapterFirmware', 'AdapterDriver']
        printTable()
            #
    def printTable():
        while True:
            print('\n\n')
            puts(colored.cyan('Available Firmware Versions: \n'))
            for result in api_response:
                versions = (result['Version'])
                print('\t' + versions)
            puts(colored.cyan('\nThis firmware query will only include ESXi version: ' + vmware_version))
            print('Enter an available UCSM Firmware Version from the list above. Example: 3.2.3 instead of 3.2(3)')
            print('If the desired firmware version is not found, try using a different VMware ESXi version.\nTo retrieve firmware versions for a different VMware ESXi version, type "New".')
            global firmwareVersion_filter
            firmwareVersion_filter = input('\nEnter firmware version: ')
            if firmwareVersion_filter == 'New':
                vmwareVersion()
            else:
                puts(colored.cyan('Firmware version entered...' + firmwareVersion_filter))
                print('\n\n')
                for bl in blade_attr_dict:
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    puts(colored.cyan(bl))
                    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                    for pid in blade_attr_dict[bl]:
                        # print pid[0][0][0][0]
                        ucsm_blade_model = pid[0][1][0][0]
                        adapter1Pid_filter = pid[0][0][0][0]
                        # print '\t' + adapter1Pid_filter
                        try:
                            adapter2Pid_filter = pid[0][0][1][0]
                        except IndexError:
                            adapter2Pid_filter = 'None'
                        # print '\t' + adapter2Pid_filter
                        break
                    for model in blade_model_ucsm_list:
                        if bl == model[0]:
                            bladeModel_filter = model[1]
                            query_list = all_list_pd[all_list_pd['BladeModels'].str.contains(bladeModel_filter) & all_list_pd['BladeFirmware'].str.contains(firmwareVersion_filter) & all_list_pd['BladeOSVersion'].str.contains(vmware_version) & all_list_pd['AdapterPid'].str.contains(adapter1Pid_filter)]
                            grouped_query = query_list.groupby(['BladeModels', 'BladeFirmware', 'AdapterPid', 'AdapterFirmware', 'AdapterDriver'])
                            if query_list.empty == True:
                                puts(colored.red('\t' + 'NO HCL RECORD FOUND IN THE API FOR THE FOLLOWING QUERY:'))
                                print('\t\t' + 'BLADE: ' + ucsm_blade_model)
                                print('\t\t' + 'ADAPTER: ' + adapter1Pid_filter)
                                print('\t\t' + 'FIRMWARE: ' + firmwareVersion_filter)
                                print('\t\t' + 'ESXi VERSION: ' + vmware_version)
                                print('\n')
                            else:
                                print(grouped_query.first())
                                print ('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                                print ('\n\n\n\n\n')
    begin()
    #
if __name__ == "__main__":
    hcl()