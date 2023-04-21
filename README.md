# Cisco IOS-XE NETCONF Smart Licensing for CSLU

## What is it ?
A solution that configures CSLU url on Cisco IOS-XE devices via NETCONF. The script adds the following configuration to the IOS-XE devices via NETCONF : 
```diff
! Authenticate the device and CSLU
license smart trust idtoken <idtoken> local

! Set up URL for device to reach CSLU
+ license smart url cslu http://<your_cslu>/cslu/v1/pi/<your_onprem_account>

! Manual synchronisation with CSLU
license smart sync local
```

<p align="center">
<img width="750" alt="image" src="https://user-images.githubusercontent.com/28600326/232914390-443da6ca-f7cc-4d1b-a6ea-e3ce77e849d5.png">
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
3. Add a ```config.yml``` file as follow:
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
                                        <url-cslu>http://<your_cslu>/cslu/v1/pi/<your_onprem_account></url-cslu>
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

<p align="center">
<img width="650" alt="image" src="https://user-images.githubusercontent.com/28600326/232914485-28bfd02d-cac9-4240-80d3-c55790c69662.png">
</p>

```xml
NETCONF Payload:
 <?xml version="1.0" encoding="utf-8"?>
<config>
        <licensing xmlns="http://cisco.com/ns/yang/cisco-smart-license">
                <config>
                        <transport>
                                <transport-cslu>
                                        <url-cslu>http://192.168.1.192/cslu/v1/pi/xvaletteOnPrem-1</url-cslu>
                                </transport-cslu>
                        </transport>
                </config>
        </licensing>
</config>

Device : STE-7ALD-WLC-1 done
```
