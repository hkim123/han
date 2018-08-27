#################################################################################################
#   Variables file
#################################################################################################

CPU_MAX=50

#ToR1_cfg="configs/ToR1.cfg"
#ToR2_cfg="configs/ToR2.cfg"
#CR_cfg="configs/CR.cfg"
#AG1_cfg="configs/spine.cfg"
cr = "CR"
ag1 = "AG1"
ag2 = "AG2"
tor1 = "ToR1"
tor2 = "ToR2"
tg1 = "TG1"


Src_Perpetual_License="license_9WHSG02"
Dst_Perpetual_License="license"
MSW_PKG_SRC="/tftpboot/users/atanu/Metaswitch/v2.4.0/cnp-base-install_2.4.0.tar.gz"
MSW_PKG_DST="cnp-base-install.tar.gz"
#
#Create Config files
#

cr_template = "cr_template.cfg"
ag1_template = "AG1_template.cfg"
ag2_template = "AG2_template.cfg"
tor1_template = "leaf1_template.cfg"
tor2_template = "leaf2_template.cfg"
cfg="/home/admin/cn_router.out"
cr_cfg = "/tftpboot/users/hkim/Coral/CR.cfg"
spine1_cfg = "/tftpboot/users/hkim/Coral/spine1.cfg"
spine2_cfg = "/tftpboot/users/hkim/Coral/spine2.cfg"
ToR1_cfg = "/tftpboot/users/hkim/Coral/leaf1.cfg"
ToR2_cfg = "/tftpboot/users/hkim/Coral/leaf2.cfg"
templatePath = "/home/hkim/art/partner-Metaswitch/L3/Config_Temp/"
tbCfgPath = "/tftpboot/users/hkim/Coral/"
#cr_intf_breakout_template = "/home/hkim/art/partner-Metaswitch/L3/Config_Temp/cr_intf_breakout.cfg"
#
# Ixia variables
#
#ixChassis='10.11.130.250'
#ixTclServer='10.156.170.253'
#ixTclServerPort = '9000'
#ixiaConfig="metaswitch.ixncfg"


#tg_config ="/home/hkim/art/partner-Metaswitch/L3/Config_Temp/metaswitch.ixncfg"
tg_config ="/tftpboot/users/hkim/Coral/metaswitch.ixncfg"
configLoadWaitTime = 180
strm_Tolerance = 300



VendorRoutes={
     "CR":17132,
     "AG1":12133,
#     "AG2":6029,
     "ToR1":17101,
     "ToR2":9063
}

KernelRoutes={
     "CR":5042,
     "AG1":5044,
#     "AG2":5040,
     "ToR1":5044,
     "ToR2":5040
}

HWRoutes={
     "CR":5041,
     "AG1":5043,
#     "AG2":5043,
     "ToR1":5043,
     "ToR2":5039
}

#EcmpRoutes={
#     "CR":4045,
#     "AG1":4047,
#     "AG2":4000,
#     "ToR1":3023,
#     "ToR2":3023
#}

Arp={
     "ToR1":4279,
     "ToR2":4275
}

OspfNeighbors={
     "AG1":26,
     "AG2":6,
     "ToR1":28,
     "ToR2":24
}

BgpNeighbors={
     "CR":18,
     "AG1":14,
     "AG2":4
}

BgpAs={
     "AG1":65501,
     "CR":65500
}
Links={
     "ToR1_to_AG1": ["e101-049-1", "e101-049-2", "e101-049-3", "e101-049-4","e101-050-1","e101-050-2","e101-050-3","e101-050-4"],
     "ToR1_to_AG2": ["e101-051-1", "e101-051-2", "e101-051-3", "e101-051-4", "e101-052-1", "e101-052-2", "e101-052-3", "e101-052-4"],
     "ToR2_to_AG1": ["e101-001-0", "e101-002-0", "e101-003-0", "e101-004-0", "e101-017-0", "e101-018-0", "e101-019-0", "e101-020-0"],
     "ToR2_to_AG2": ["e101-005-0", "e101-006-0", "e101-007-0", "e101-008-0", "e101-021-0", "e101-022-0", "e101-023-0", "e101-024-0"],
     "AG1_to_CR": ["e101-013-0", "e101-014-0", "e101-015-0", "e101-016-0", "e101-029-0", "e101-030-0", "e101-031-0", "e101-032-0"],
     "CR_to_AG2": ["e101-005-1", "e101-006-1", "e101-007-1", "e101-008-1", "e101-021-1", "e101-022-1", "e101-023-1", "e101-024-1"]
}
