*** Settings ***


Documentation     Metaswitch L3 Use Case
Force Tags        pd  dell_cli  frid-3352


Metadata          Script_Author               Han Kim
Metadata          Script_Date
Metadata          Script_Test_Type
Metadata          Script_Module
Metadata          Script_Reviewer             Han_Kim@Dell.com
Metadata          Script_min_Release
Metadata          Script_min_Version
Metadata          Script_max_Version
Metadata          Script_Requirements
Metadata          Script_Testbed
Metadata          Script_Notes
Metadata          Script_Usage

# Above file is required for interfaces verification
Variables         l3_variable.py

Library           OperatingSystem
Library           robotParser.py
Library           ScriptLib/Miscellaneous/deparameterizingConfig.py
Library           ScriptLib/Miscellaneous/changeStreamAttributes.py
Library           ScriptLib/IPServicesLib/fileTransferProtocol.py
Library           Collections
Library           ScriptLib/Miscellaneous/changeStreamAttributes.py
Library           ScriptLib/Miscellaneous/executeCli.py
Library           ScriptLib/IPServicesLib/fileTransferProtocol.py
Library           ScriptLib/IPServicesLib/connectSessionType.py
Library           ShowParserLib/showVersion.py
Library           ScriptTopoModule
Library           metaswitch_lib.py
#Library           IxNetwork_lib.py
Library           Collections
Library           String
Library           TrafficGenLib/TG_ExportImport.py
Library           TrafficGenLib/TG_Port.py
Library           TrafficGenLib/TG_Protocol.py
Library           TrafficGenLib/TG_Stream.py
Library           TrafficGenLib/TG_Stats.py
Library           TrafficGenLib/TG_Capture.py
Library           TrafficGenLib/TG_Disconnect.py
Library           TrafficGenLib/trafficLib.py
Library           TrafficGenLib/trafficUtils.py
Library           TrafficGenLib/bandwidth.py
Library           TrafficGenLib/TG_Router_BGP.py
Library           statsCompare

Suite Setup       Prepare required setup
Suite Teardown    disconnect_script_topology_devices

*** Test Cases ***
Test1.0
    [Documentation]  Create Configuration File
    #...    Generating Configuration files to TFTP paths
    #...    Testcase ID  -
    Step  1  Create Configuration Files

Test 1.1
    [Documentation]  Verify Clean install
    #...    Testcase Name - Verify clean install
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  2    Install Vendor Packages in CR with Abort 0
    Step  3    Verify Vendor Processes in CR

Test 1.2
    [Documentation]  Abort during the install and re-install
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  2    Install Vendor Packages in CR with Abort 1
    Step  3    Install Vendor Packages in CR with Abort 0
    Step  4    Verify Vendor Processes in CR

Test 1.3
    [Documentation]  Remove files and re-install
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  2    Install Vendor Packages in CR with Abort 0
    Step  3    Remove files in CR
    Step  4    Install Vendor Packages in CR with Abort 0
    Step  5    Verify Vendor Processes in CR

Test 1.4
    [Documentation]  Upgrade packages
    #...    Testcase ID  -

#    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  2    Upgrade Vendor Packages in CR with Abort 0
    Step  3    Verify Vendor Processes in CR

Test 1.5
    [Documentation]  Abort during upgrade and upgrade again.
    #...    Testcase ID  -

    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  2    Upgrade Vendor Packages in CR with Abort 1
    Step  3    Upgrade Vendor Packages in CR with Abort 0
    Step  4    Verify Vendor Processes in CR

Test 1.7
    [Documentation]  Uninstall packages and re-install
    #...    Testcase ID  -

    Step  1    UnInstall Vendor Packages in CR
    Step  2    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
    Step  3    Install Vendor Packages in CR with Abort 0
    Step  4    Copy license file in CR
    Step  5    Verify perpetual license ${Dst_Perpetual_License} in CR
    Step  6    Verify Vendor Processes in CR

Test 1.8

    [Documentation]  Verify Clean install on all switches
    #...    Testcase Name - Verify clean install on all switches
    #...    Testcase ID  -

#    Step  1    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
#    Step  2    Install Vendor Packages in CR with Abort 0
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

#Test 1.9
#    [Documentation]  Install perpetual license
    #...    Testcase ID  -

#    Step  1    Copy File To Switch ${Src_Perpetual_License} to ${Dst_Perpetual_License} in CR
#    Step  2    Copy File To Switch ${MSW_PKG_SRC} to ${MSW_PKG_DST} in CR
#    Step  1    Verify perpetual license ${Dst_Perpetual_License} in CR

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
    Step  1    Copy File To Switch ${spine1_cfg} to ${cfg} in AG1
    Step  2    Load Config ${cfg} on AG1

Test 1.13
    [Documentation]  Copy the config file to CR
    #...    Testcase ID  -
    Step  1    Copy File To Switch ${CR_cfg} to ${cfg} in CR
    Step  2    Load Config ${cfg} on CR

Test 1.14
    [Documentation]  Load the config file to ixia
    #...    Testcase ID  -
    Step  1    Perform Action  ${tg1}  disconnect
    Step  2    TG_Load_Config  ${tg1}  ${tg_config}
    Step  3    TG_Test_Control  ${tg1}  start_all_protocols
    Step  4    Sleep  180  seconds
#    Step  5    TG_Test_Control  ${tg1}  stop_all_protocols
    Step  5    TG_Traffic_Control  ${tg1}  apply
    Step  6    TG_Traffic_Control  ${tg1}  run
    Step  7    Sleep  60  seconds
    Step  8    TG_Traffic_Control  ${tg1}  stop
    Step  9    Sleep  30  seconds
    Step  10   TG_Traffic_Control  ${tg1}  run
    Step  11   Sleep  180  seconds
    Step  12   Verify Traffic


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
    [Documentation]  Verify BGP
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

Test1.21
    #[Documentation] interface errors
    #...    Testcase ID  -

    Step  1    Check Interface errors in ToR1
    Step  2    Check Interface errors in ToR2
    Step  3    Check Interface errors in AG1
    #Step  4    Check Interface errors in AG2
    Step  5    Check Interface errors in CR

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
    Step  3    Sleep  120  seconds
    Step  4    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  5    Check Memory in ToR1
    Step  6    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  7    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  8    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  9    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  10   Check ARP in ToR1 ${Arp["ToR1"]}
    Step  11   Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  12   Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  13   Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  14   Check Routes in BCM on AG1 ${HWRoutes["AG1"]}
    step  15   Verify Traffic


Test2.2
    #[Documentation]
    #...    Testcase Name - Link flap between ToR1 and AG2
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["ToR1_to_AG2"]} in ToR1
    Step  2    NoShut interface ${Links["ToR1_to_AG2"]} in ToR1
    Step  3    Sleep  120  seconds
    Step  4    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  5    Check Memory in ToR1
    Step  6    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  7    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  8    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  9    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  10   Check ARP in ToR1 ${Arp["ToR1"]}
    step  11   Verify Traffic


Test2.3
    #[Documentation]
    #...    Testcase Name - Link flap between AG1 and ToR2
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["ToR2_to_AG1"]} in ToR2
    Step  2    NoShut interface ${Links["ToR2_to_AG1"]} in ToR2
    Step  3    Sleep  120  seconds
    Step  4    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  5    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  6    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  7    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  8    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}
    Step  9    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  10   Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  11   Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  12   Check Routes in BCM on AG1 ${HWRoutes["AG1"]}
    Step  13   Check Memory in ToR2
    Step  14   Check Arp in ToR2 ${Arp["ToR2"]}
    step  15   Verify Traffic

Test2.4
    #[Documentation]
    #...    Testcase Name - Link flap between ToR2 and AG2
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["ToR2_to_AG2"]} in ToR2
    Step  2    NoShut interface ${Links["ToR2_to_AG2"]} in ToR2
    Step  3    Sleep  120  seconds
    Step  4    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  5    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  6    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  7    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  8    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}
    Step  9    Check Memory in ToR2
    Step  10   Check Arp in ToR2 ${Arp["ToR2"]}
    step  16   Verify Traffic

Test2.5
    #[Documentation]
    #...    Testcase Name - Link flap between AG1 and CR
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["AG1_to_CR"]} in AG1
    Step  2    NoShut interface ${Links["AG1_to_CR"]} in AG1
    Step  3    Sleep  120  seconds
    Step  4    Check CPU in AG1 for max CPU ${CPU_MAX}
    Step  5    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  6    Check BGP Neighbors in AG1 ${BgpAs["AG1"]} ${BgpNeighbors["AG1"]}
    Step  7    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  8    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  9    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}
    Step  10   Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  11   Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  12   Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  13   Check Routes in BCM on CR ${HWRoutes["CR"]}
    Step  14   Check Memory in AG1
    step  15   Verify Traffic

Test2.6
    #[Documentation]
    #...    Testcase Name - Link flap between AG2 and CR
    #...    Testcase ID  -

    #missing check traffic
    Step  1    Shut interface ${Links["CR_to_AG2"]} in CR
    Step  2    NoShut interface ${Links["CR_to_AG2"]} in CR
    Step  3    Sleep  120  seconds
    Step  4    Check CPU in CR for max CPU ${CPU_MAX}
    Step  5    Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  6    Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  7    Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  8    Check Routes in BCM on CR ${HWRoutes["CR"]}
    Step  9    Check Memory in CR
    step  10   Verify Traffic


Test3.1
    #[Documentation]
    #...    Testcase Name - Reboot  ToR1
    #...    Testcase ID  -

    Step  1    Reboot ToR1
    Step  2    Check CPU in ToR1 for max CPU ${CPU_MAX}
    Step  3    Check Memory in ToR1
    Step  4    Sleep  120  seconds
    Step  5    Check OSPF Neighbors in ToR1 ${OspfNeighbors["ToR1"]}
    Step  6    Check Routes using vendor cli on ToR1 ${VendorRoutes["ToR1"]}
    Step  7    Check Routes in kernel on ToR1 ${KernelRoutes["ToR1"]}
    Step  8    Check Routes in BCM on ToR1 ${HWRoutes["ToR1"]}
    Step  9    Check ARP in ToR1 ${Arp["ToR1"]}

Test3.2
    #[Documentation]
    #...    Testcase Name - Reboot  ToR2
    #...    Testcase ID  -

    Step  1    Reboot ToR2
    Step  2    Check CPU in ToR2 for max CPU ${CPU_MAX}
    Step  3    Check Memory in ToR2
    Step  4    Sleep  120  seconds
    Step  5    Check OSPF Neighbors in ToR2 ${OspfNeighbors["ToR2"]}
    Step  6    Check Routes using vendor cli on ToR2 ${VendorRoutes["ToR2"]}
    Step  7    Check Routes in kernel on ToR2 ${KernelRoutes["ToR2"]}
    Step  8    Check Routes in BCM on ToR2 ${HWRoutes["ToR2"]}
    Step  9    Check ARP in ToR2 ${Arp["ToR2"]}

Test3.3
    #[Documentation]
    #...    Testcase Name - Reboot  AG1
    #...    Testcase ID  -

    Step  1    Reboot AG1
    Step  2    Check CPU in AG1 for max CPU ${CPU_MAX}
    Step  3    Check Memory in AG1
    Step  4    Sleep  120  seconds
    Step  5    Check OSPF Neighbors in AG1 ${OspfNeighbors["AG1"]}
    Step  6    Check Routes using vendor cli on AG1 ${VendorRoutes["AG1"]}
    Step  7    Check Routes in kernel on AG1 ${KernelRoutes["AG1"]}
    Step  8    Check Routes in BCM on AG1 ${HWRoutes["AG1"]}

Test3.4
    #[Documentation]
    #...    Testcase Name - Reboot  CR
    #...    Testcase ID  -

    Step  1    Reboot CR
    Step  2    Check CPU in CR for max CPU ${CPU_MAX}
    Step  3    Check Memory in CR
    Step  4    Sleep  120  seconds
    Step  5    Check BGP Neighbors in CR ${BgpAs["CR"]} ${BgpNeighbors["CR"]}
    Step  6    Check Routes using vendor cli on CR ${VendorRoutes["CR"]}
    Step  7    Check Routes in kernel on CR ${KernelRoutes["CR"]}
    Step  8    Check Routes in BCM on CR ${HWRoutes["CR"]}

*** Keywords ***

Prepare required setup
    connect to script topology devices

Create Configuration Files
    convert_template_to_config  ${cr}  ${templatePath}  ${tbCfgPath}  ${cr_template}  ${cr_cfg}
    convert_template_to_config  ${ag1}  ${templatePath}  ${tbCfgPath}  ${ag1_template}  ${spine1_cfg}
    convert_template_to_config  ${ag2}  ${templatePath}  ${tbCfgPath}  ${ag2_template}  ${spine2_cfg}
    convert_template_to_config  ${tor1}  ${templatePath}  ${tbCfgPath}  ${tor1_template}  ${ToR1_cfg}
    convert_template_to_config  ${tor2}  ${templatePath}  ${tbCfgPath}  ${tor2_template}  ${ToR2_cfg}

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

Copy license file in ${device}
    copy_license_file  ${device}

Verify Vendor Processes in ${device}
    verify_vendor_processes  ${device}

Reboot ${device}
    switch_reboot  ${device}

Verify SSH to ${device}
    connect_ssh  ${device}

Check Interface errors in ${device}
    check_interface_errors  ${device}

#Verify Evaluation License in ${device}
#    verify_eval_license  ${device}

Remove files in ${device}
    remove_vendor_files  ${device}

Verify perpetual license ${lic} in ${device}
    verify_perpetual_license  ${lic}  ${device}

Copy File To Switch ${src} to ${dst} in ${device}
    copy_file_to_switch  ${src}  ${dst}  ${device}

Load Config ${cfg} on ${device}
    load_cfg  ${cfg}  ${device}

Verify Traffic
     ${tx_pkt_rate_tr1} =  TG_Flow_Based_Stats  ${tg1}  TG1_ToR1_3  aggregate.tx.pkt_rate
     ${int_tx_pkt_rate_tr1} =  Convert To Number  ${tx_pkt_rate_tr1}
     ${rx_pkt_rate_tr1} =  TG_Flow_Based_Stats  ${tg1}  TG1_ToR2_3  aggregate.rx.pkt_rate
     ${int_rx_pkt_rate_tr1}=  Convert To Number  ${rx_pkt_rate_tr1}
     ${result_west_east} =  Compare Stats  ${int_rx_pkt_rate_tr1}   ${int_tx_pkt_rate_tr1}   ${strm_Tolerance}
     Run Keyword And Continue On Failure  Run Keyword If  "${result_west_east}" == "FAIL"  FAIL  "Expected frame rate not received on ToR2 "
     ${tx_pkt_rate_tr2} =  TG_Flow_Based_Stats  ${tg1}  TG1_ToR2_3  aggregate.tx.pkt_rate
     ${int_tx_pkt_rate_tr2} =  Convert To Number  ${tx_pkt_rate_tr2}
     ${rx_pkt_rate_tr2} =  TG_Flow_Based_Stats  ${tg1}  TG1_ToR1_3  aggregate.rx.pkt_rate
     ${int_rx_pkt_rate_tr2} =  Convert To Number  ${rx_pkt_rate_tr2}
     ${result_east_west} =  Compare Stats  ${int_rx_pkt_rate_tr2}   ${int_tx_pkt_rate_tr2}   ${strm_Tolerance}
     Run Keyword And Continue On Failure  Run Keyword If  "${result_east_west}" == "FAIL"  FAIL  "Expected frame rate not received on ToR1 "
