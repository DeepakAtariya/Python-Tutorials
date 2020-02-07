import subprocess as sp
import optparse 
import re

def get_parameter():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an MAC address, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for "+interface+" to "+new_mac)

    # sp.call("ifconfig "+interface+" down", shell=True)
    # sp.call("ifconfig "+interface+" hw ether "+new_mac, shell=True)
    # sp.call("ifconfig "+interface+" up", shell=True)

    sp.call(["ifconfig",interface,"down"])
    sp.call(["ifconfig",interface,"hw","et her",new_mac])
    sp.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    ifconfig_result = sp.check_output(["ifconfig", interface])
    # print(ifconfig_result)
    mac_address_search_result = re.search(rb"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")

options = get_parameter()

interface = options.interface
new_mac = options.new_mac
current_mac = get_current_mac(interface)
print("Current MAC = "+str(current_mac))
change_mac(interface, new_mac)

