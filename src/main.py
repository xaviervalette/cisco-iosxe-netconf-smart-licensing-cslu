# Import necessary libraries
from ncclient import manager
import yaml
from xml.dom import minidom 
import xmltodict
import sys

# Open the configuration YAML file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

with open("conf/cslu.xml", 'r') as file:
    csluXml = xmltodict.parse(file.read())

csluXml["config"]["licensing"]["config"]["transport"]["transport-cslu"]["url-cslu"] = config["cslu"]["url"]

cslu = xmltodict.unparse(csluXml, pretty = True)

print ("NETCONF Payload:\n", cslu, '\n')

# Set up device info
for device in config["iosXeDevice"]:
    username = device["username"]
    password = device["password"]
    port = device["port"]
    host = device["host"]
    device_params = {"name": "iosxe"}

    # Connect to the device and retrieve its configuration, then parse and format the output
    with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as netconf_manager:
        edit_config_response = netconf_manager.edit_config(cslu, target='running')
    print("Device :", device["name"], "done")
        
