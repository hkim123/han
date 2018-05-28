*** Settings ***


Documentation     Metaswitch L3 Use Case
Force Tags        pd  dell_cli  frid-3352


Metadata          Script_Author               Mallikarjuna Rapuru
Metadata          Script_Date
Metadata          Script_Test_Type
Metadata          Script_Module
Metadata          Script_Reviewer             Mallikarjuna_Rapuru@Dell.com
Metadata          Script_min_Release
Metadata          Script_min_Version
Metadata          Script_max_Version
Metadata          Script_Requirements
Metadata          Script_Testbed
Metadata          Script_Notes
Metadata          Script_Usage

# Above file is required for interfaces verification
Variables         l3_variable.py

Library           ScriptTopoModule
Library           metaswitch_lib.py
Library           IxNetwork_lib.py
Library           Collections
Library           String

Suite Setup       Prepare required setup
Suite Teardown    disconnect_script_topology_devices

*** Test Cases ***

Test Load_start_IXIA
    [Documentation]  Load ixia config on IxNetwork
    #...    Testcase Name - Load ixia config on IxNetwork
    #...    Testcase ID  -

    Step  1   Load IxNetwork Config ${ixChassis} ${ixTclServer} ${ixTclServerPort} ${ixiaConfig}


Test 1.1
    [Documentation]  Verify Clean install
    #...    Testcase Name - Verify clean install
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  2    Install Vendor Packages in TMPR with Abort 0
    Step  3    Verify Vendor Processes in TMPR

Test 1.2
    [Documentation]  Abort during the install and re-install
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  2    Install Vendor Packages in TMPR with Abort 1
    Step  3    Install Vendor Packages in TMPR with Abort 0
    Step  4    Verify Vendor Processes in TMPR

Test 1.3
    [Documentation]  Remove files and re-install
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  2    Install Vendor Packages in TMPR with Abort 0
    Step  3    Remove files in TMPR
    Step  4    Install Vendor Packages in TMPR with Abort 0
    Step  5    Verify Vendor Processes in TMPR

Test 1.4
    [Documentation]  Upgrade packages
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  2    Upgrade Vendor Packages in TMPR with Abort 0
    Step  3    Verify Vendor Processes in TMPR

Test 1.5
    [Documentation]  Abort during upgrade and upgrade again.
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  2    Upgrade Vendor Packages in TMPR with Abort 1
    Step  3    Upgrade Vendor Packages in TMPR with Abort 0
    Step  4    Verify Vendor Processes in TMPR

Test 1.7
    [Documentation]  Uninstall packages and re-install
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  2    UnInstall Vendor Packages in TMPR
    Step  3    Install Vendor Packages in TMPR with Abort 0
    Step  4    Verify Vendor Processes in TMPR

Test 1.8

    [Documentation]  Verify Clean install on all switches
    #...    Testcase Name - Verify clean install on all switches
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  2    Install Vendor Packages in CR with Abort 0
    Step  3    Verify Vendor Processes in CR
    Step  4    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in AG1
    Step  5    Install Vendor Packages in AG1 with Abort 0
    Step  6    Verify Vendor Processes in AG1
    Step  7    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in ToR1
    Step  8    Install Vendor Packages in ToR1 with Abort 0
    Step  9    Verify Vendor Processes in ToR1
    Step  10    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in ToR2
    Step  11    Install Vendor Packages in ToR2 with Abort 0
    Step  12    Verify Vendor Processes in ToR2

Test 1.9
    [Documentation]  Install perpetual license
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${Src_Perpetual_License} to ${Dst_Perpetual_License} in TMPR
    Step  2    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR
    Step  3    Verify perpetual license ${Dst_Perpetual_License} in TMPR

Test 1.10
    [Documentation]  Copy the config file to ToR1
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${ToR1_cfg} to ${cfg} in ToR1
    Step  2    Load Config ${cfg} on ToR1

Test 1.11
    [Documentation]  Copy the config file to ToR2
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${ToR2_cfg} to ${cfg} in ToR2
    Step  2    Load Config ${cfg} on ToR2

Test 1.12
    [Documentation]  Copy the config file to AG1
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${AG1_cfg} to ${cfg} in AG1
    Step  2    Load Config ${cfg} on AG1

Test 1.13
    [Documentation]  Copy the config file to CR
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${CR_cfg} to ${cfg} in CR
    Step  2    Load Config ${cfg} on CR

Test1.15
    [Documentation]  Verify OSPF on ToR1 and ToR2
    #...    Testcase ID  -

    Step  1    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  2    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  3    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  4    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  5    Check ARP in ToR1 ${Arp["ToR1"]}
    Step  6    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  7    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  8    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  9    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}
    Step  10   Check ARP in ToR2 ${Arp["ToR2"]}

Test1.16
    [Documentation]  Verify OSPF on AG1
    #...    Testcase ID  -

    Step  1    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  2    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  3    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  4    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}

Test1.17
    [Documentation]  Verify EBGP
    #...    Testcase ID  -

    Step  1    Check BGP Neighbors in AG1 ${BgpAs["AG1"]} ${BgpNeighbors["AG1"]}
    Step  2    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  3    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  4    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}
    Step  5    Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  6    Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  7    Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  8    Check Routes in BCM on CR ${HWRoutes["CR"]}

#1.18 -- ECMP
#1.19 -- Traffic

Test1.20
    [Documentation]  Verify CPU Usage
    #...    Testcase ID  -

    Step  1    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  2    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  3    Check CPU in AG1 for max CPU ${CPU_MAX}
    #Step  4    Check CPU in AG2 for max CPU ${CPU_MAX}
    Step  5    Check CPU in CR for max CPU ${CPU_MAX}

#1.21 -- interface statistics
Test1.21
    #[Documentation]
    #...    Testcase Name - Verify CPU Usage
    #...    Testcase ID  -

    Step  1    Check Interface Statistics in ToR1
    Step  2    Check Interface Statistics in ToR2
    Step  3    Check Interface Statistics in AG1
    #Step  4    Check Interface Statistics in AG2
    Step  5    Check Interface Statistics in CR

Test2.1
    #[Documentation]
    #...    Testcase Name - Link flap between ToR1 and AG1
    #...    Testcase ID  -

    #missing check traffic
    #:FOR    ${ELEMENT}    IN    ${Links["ToR1_to_AG1"}
    #\    Log    ${ELEMENT}
#
    Step  1    Shut interface ${Links["ToR1_to_AG1"]} in ToR1
    Step  2    NoShut interface ${Links["ToR1_to_AG1"]} in ToR1
    Step  3    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  4    Check Memory in ToR1
    Step  5    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  6    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  7    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  8    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  9    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  10    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  11    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  12    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}
    Step  13    Check ARP in ToR1 ${Arp["ToR1"]}

Test2.2
    #[Documentation]
    #...    Testcase Name - Link flap between ToR1 and AG2
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["ToR1_to_AG2"]} in ToR1
    Step  2    NoShut interface ${Links["ToR1_to_AG2"]} in ToR1
    Step  3    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  4    Check Memory in ToR1
    Step  5    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  6    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  7    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  8    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  9    Check ARP in ToR1 ${Arp["ToR1"]}


Test2.3
    #[Documentation]
    #...    Testcase Name - Link flap between AG1 and ToR2
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["ToR2_to_AG1"]} in ToR2
    Step  2    NoShut interface ${Links["ToR2_to_AG1"]} in ToR2
    Step  3    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  4    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  5    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  6    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  7    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}

    Step  8    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  9    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  10    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  11    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}
    Step  12    Check Memory in ToR2
    Step  13    Check Arp in ToR2 ${Arp["ToR2"]}

Test2.4
    #[Documentation]
    #...    Testcase Name - Link flap between ToR2 and AG2
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["ToR2_to_AG2"]} in ToR2
    Step  2    NoShut interface ${Links["ToR2_to_AG2"]} in ToR2
    Step  3    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  4    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  5    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  6    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  7    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}
    Step  8    Check Memory in ToR2
    Step  9    Check Arp in ToR2 ${Arp["ToR2"]}

Test2.5
    #[Documentation]
    #...    Testcase Name - Link flap between AG1 and CR
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["AG1_to_CR"]} in AG1
    Step  2    NoShut interface ${Links["AG1_to_CR"]} in AG1

    Step  3    Check CPU in AG1 for max CPU ${CPU_MAX}
    Step  4    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  5    Check BGP Neighbors in AG1 ${BgpAs["AG1"]} ${BgpNeighbors["AG1"]}
    Step  6    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  7    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  8    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}

    Step  9    Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  10    Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  11    Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  12    Check Routes in BCM on CR ${HWRoutes["CR"]}
    Step  13    Check Memory in AG1

Test2.6
    #[Documentation]
    #...    Testcase Name - Link flap between AG2 and CR
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["CR_to_AG2"]} in CR
    Step  2    NoShut interface ${Links["CR_to_AG2"]} in CR
    Step  3    Check CPU in CR for max CPU ${CPU_MAX}
    Step  4    Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  5    Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  6    Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  7    Check Routes in BCM on CR ${HWRoutes["CR"]}
    Step  8    Check Memory in CR


Test3.1
    #[Documentation]
    #...    Testcase Name - Reboot  ToR1
    #...    Testcase ID  -

    Step  1    Reboot ToR1
    Step  2    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  3    Check Memory in ToR1
    Step  4    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  5    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  6    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  7    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  8    Check ARP in ToR1 ${Arp["ToR1"]}

Test3.2
    #[Documentation]
    #...    Testcase Name - Reboot  ToR2
    #...    Testcase ID  -

    Step  1    Reboot ToR2
    Step  2    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  3    Check Memory in ToR2
    Step  4    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  5    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  6    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  7    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}
    Step  8    Check ARP in ToR2 ${Arp["ToR2"]}

Test3.3
    #[Documentation]
    #...    Testcase Name - Reboot  AG1
    #...    Testcase ID  -

    Step  1    Reboot AG1
    Step  2    Check CPU in AG1 for max CPU ${CPU_MAX}
    Step  3    Check Memory in AG1
    Step  4    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  5    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  6    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  7    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}

Test3.4
    #[Documentation]
    #...    Testcase Name - Reboot  CR
    #...    Testcase ID  -

    Step  1    Reboot CR
    Step  2    Check CPU in CR for max CPU ${CPU_MAX}
    Step  3    Check Memory in CR
    Step  4    Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  5    Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  6    Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  7    Check Routes in BCM on CR ${HWRoutes["CR"]}

*** Keywords ***

Prepare required setup
    connect to script topology devices  # this is the command to connect using metaswitch.yaml file. default is console connect

Clear the system logs in ${device}
    clear_syslog_messages  ${device}

Check CPU in ${device} for max CPU ${cpu_max}
    check_cpu  ${device}  ${cpu_max}

Check Memory in ${device}
    check_mem  ${device}

Check Routes in BCM on ${device} ${routes}
    check_bcm_routes  ${device}  ${routes}

Check Routes in kernel on ${device} ${routes}
    check_kernel_routes  ${device}  ${routes}

Check Routes using vendor cli on ${device} ${routes}
    check_vendor_routes  ${device}  ${routes}

Check ARP in ${device} ${arps}
    check_arp  ${device}  ${arps}

Shut interface ${iface} in ${device}
    link_shut  ${device}  ${iface}

NoShut interface ${iface} in ${device}
    link_up  ${device}  ${iface}

Check OSPF Neighbors in ${device} ${neighbors}
    check_ospf_neighbors  ${device}  ${neighbors}

Check BGP Neighbors in ${device} ${as} ${nbrs}
    check_bgp_neighbors  ${device}  ${as}  ${nbrs}

Upgrade Vendor Packages in ${device} with Abort ${abort}
    upgrade_vendor_packages  ${device}  ${abort}

Install Vendor Packages in ${device} with Abort ${abort}
    clean_install_vendor_packages  ${device}  ${abort}

UnInstall Vendor Packages in ${device}
    uninstall_vendor_packages  ${device}

Verify Vendor Processes in ${device}
    verify_vendor_processes  ${device}

Reboot ${device}
    switch_reboot  ${device}

Verify SSH to ${device}
    connect_ssh  ${device}

Check Interface Statistics in ${device}
    check_interface_statistics  ${device}

Verify Evaluation License in ${device}
    verify_eval_license  ${device}

Remove files in ${device}
    remove_vendor_files  ${device}

Verify perpetual license ${lic} in ${device}
    verify_perpetual_license  ${lic}  ${device}

Copy File To Switch ${src} to ${dst} in ${device} # This is not only description, the variable ${src} & ${dst} should match below line
    copy_file_to_switch  ${src}  ${dst}  ${device}  # this is also NGF command to give 3 argument ${src},${dst},${device} which is on test 1.1 step 1 ${MSW_PKG_SRC} to ${MSW_PKG_DST} in TMPR, so {src} is ${MSW_PKG_SRC} and ${dst} is ${MSW_PKG_DST} and ${device} is the device under metaswitch.yaml under TMPR

Load Config ${cfg} on ${device}
    load_cfg  ${cfg}  ${device}

Load IxNetwork Config ${ixChassis} ${ixTclServer} ${ixTclServerPort} ${ixiaConfig}
    load_ixnetwork_cfg  ${ixChassis}  ${ixTclServer}  ${ixTclServerPort}  ${ixiaConfig}
