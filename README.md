# Cisco IOS-XE NETCONF Smart Licensing for CSLU

## What is it ?
A solution that configures CSLU url on Cisco IOS-XE devices via NETCONF. The script adds the following configuration to the IOS-XE devices via NETCONF : 
```console
license smart url cslu http://<your_cslu>:8182/cslu/v1/pi
```
<p align="center">
<img width="650" alt="image" src="https://user-images.githubusercontent.com/28600326/232494010-f91e2b7d-1902-4a49-89e9-050a9d98eb8e.png">
</p>

## Prerequisites
- IOS-XE device with NETCONF enabled
- CSLU (SSM On-Prem, Windows app, DNA Center, ...) that should be reachable from IOS-XE device

## Get started
1. Clone or download this repo
```console
git clone https://github.com/xaviervalette/cisco-iosxe-netconf-smart-licensing-cslu
```
2. Install required packages
```console
python3 -m pip install -r requirements.txt
```
3. Add a ```config.yml``` file and a ```log``` folder as follow:
```diff
└── meraki-network-event-log-collector/
+   ├── config.yml
    ├── src/
    │   └── main.py  
    └── conf/
        └── cslu.xml
```
4. In the ```config.yml``` file, add the following variables:
```yaml
#config.yml
---
cslu:
    url: "http://<your_cslu>:8182/cslu/v1/pi"
iosXeDevice:
  - name: "<iosxe_device_1>"
    username: "<...>"
    password: "<...>"
    port: "<netconf_port (default 830)>"
    host: "<ip_addr_1>"

  - name: "<iosxe_device_2>"
    username: "<...>"
    password: "<...>"
    port: "<netconf_port (default 830)>"
    host: "<ip_addr_2>"

    # ...

  - name: "<iosxe_device_n>"
    username: "<...>"
    password: "<...>"
    port: "<netconf_port (default 830)>"
    host: "<ip_addr_n>"

...

```

5. Now you can run the code by using the following command:
```console
python3 src/main.py
```

## Output
The output should be as followed:
```xml
NETCONF Payload:
 <?xml version="1.0" encoding="utf-8"?>
<config>
        <licensing xmlns="http://cisco.com/ns/yang/cisco-smart-license">
                <config>
                        <transport>
                                <transport-cslu>
                                        <url-cslu>http://<your_cslu:8182>/cslu/v1/pi</url-cslu>
                                </transport-cslu>
                        </transport>
                </config>
        </licensing>
</config>

Device : iosxe_device_1 done
Device : iosxe_device_2 done
[...]
Device : iosxe_device_n done
```

Example:
```xml
NETCONF Payload:
 <?xml version="1.0" encoding="utf-8"?>
<config>
        <licensing xmlns="http://cisco.com/ns/yang/cisco-smart-license">
                <config>
                        <transport>
                                <transport-cslu>
                                        <url-cslu>http://192.168.0.42:8182/cslu/v1/pi</url-cslu>
                                </transport-cslu>
                        </transport>
                </config>
        </licensing>
</config>

Device : STE-7ALD-WLC-1 done
```
