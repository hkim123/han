#!/usr/bin/python
# Copyright (c) 2016 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED ON AN  *AS IS* BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT
# LIMITATION ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS
# FOR A PARTICULAR PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.

import subprocess
import sys
import re
ifconfig_output = subprocess.check_output(['ip', 'link', 'show'])
ifconfig_output_list = ifconfig_output.split('\n')
kernel_intf_list = []
for item in ifconfig_output_list:
	kernel_intf_name_search = re.search(r': (e\d+-\d+-\d+):', item)
	if kernel_intf_name_search:
		kernel_intf_name = kernel_intf_name_search.group(1)
		kernel_intf_list.append(kernel_intf_name)
hw_port_list = []
for intf_name in kernel_intf_list:
	linkshow_output = subprocess.check_output("ip link show " + intf_name,shell=True)
	hw_port_search = re.search(r"alias NAS## 0 (\d+)", linkshow_output)
	if hw_port_search:
		hw_port = hw_port_search.group(1)
    	else:
        	hw_port = "NotConnected"
	hw_port_list.append(hw_port)
logical_port_list = []
for port in hw_port_list:
    	if port=="NotConnected":
        	logical_port = "NotConnected"
    	else:
		hw_port_pattern = "hw_port=\"" + str(port) + "\""
		init_xml_output = subprocess.check_output(['grep', hw_port_pattern, '/etc/opx/sai/init.xml'])
		logical_port_search = re.search(r"logical_port=\"(\d+)\"", init_xml_output)
		if logical_port_search:
			logical_port = logical_port_search.group(1)
	logical_port_list.append(logical_port)
bcm_port_list = []
bcm_command = '"ps"'
hshell_output = subprocess.check_output("sudo hshell -c " + bcm_command,stderr=subprocess.STDOUT,shell=True)
for logi_port in logical_port_list:
    	if logi_port=="NotConnected":
        	bcm_port="NotConnected"
    	else:
	    	pattern = r'(\S+\d+)\( *' + logi_port + '\)'
	    	bcm_port_search = re.search(pattern,hshell_output)
	    	if bcm_port_search:
		    	bcm_port = bcm_port_search.group(1)
	bcm_port_list.append(bcm_port)
print("%15s%15s%15s%15s" % ('FrontEndPort','HWPort','LogicalPort','BCMPort'))
print("%15s%15s%15s%15s" % ('============','======','===========','======='))
row_list = []
for (kernel_port, hw_port, logical_port, bcm_port) in zip(kernel_intf_list, hw_port_list, logical_port_list,bcm_port_list):
	print("%15s%15s%15s%15s" % (kernel_port, hw_port, logical_port, bcm_port))	
