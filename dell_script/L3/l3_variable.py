#################################################################################################
#   Variables file
#################################################################################################

CPU_MAX=50

ToR1_cfg="configs/ToR1.cfg"
ToR2_cfg="configs/ToR2.cfg"
CR_cfg="configs/CR.cfg"
AG1_cfg="configs/spine.cfg"
cfg="/home/admin/cn_router.out"
Src_Perpetual_License="license_7604XC2"
Dst_Perpetual_License="license"
MSW_PKG_SRC="/tftpboot/users/atanu/Metaswitch/v1.0.2-lacp/nst-eval-install_1.0.2-lacp.tar.gz"

#
# Ixia variables
#
ixChassis='10.11.130.250'
ixTclServer='10.156.170.253'
ixTclServerPort = '9000'
ixiaConfig="configs/metaswitch.ixncfg"


MSW_PKG_DST="nst-eval-install.tar.gz"

VendorRoutes={
     "CR":13166,
     "AG1":10163,
     "AG2":4000,
     "ToR1":13132,
     "ToR2":8080
}

KernelRoutes={
     "CR":4056,
     "AG1":4053,
     "AG2":4000,
     "ToR1":4056,
     "ToR2":4052
}

HWRoutes={
     "CR":4052,
     "AG1":4052,
     "AG2":4000,
     "ToR1":4056,
     "ToR2":4051
}

EcmpRoutes={
     "CR":4045,
     "AG1":4047,
     "AG2":4000,
     "ToR1":3023,
     "ToR2":3023
}

Arp={
     "ToR1":4249,
     "ToR2":4755
}

OspfNeighbors={
     "AG1":26,
     "AG2":20,
     "ToR1":28,
     "ToR2":4
}
       
BgpNeighbors={
     "CR":20,
     "AG1":4,
     "AG2":10
}

BgpAs={
     "AG1":65501,
     "CR":65500
}
Links={
     "ToR1_to_AG1": ["e101-049-1", "e101-049-2", "e101-049-3", "e101-049-4"],
     "ToR1_to_AG2": ["e101-051-1", "e101-051-2", "e101-051-3", "e101-051-4", "e101-052-1", "e101-052-2", "e101-052-3", "e101-052-4"],
     "ToR2_to_AG1": ["e101-001-0", "e101-002-0", "e101-003-0", "e101-004-0", "e101-017-0", "e101-018-0", "e101-019-0", "e101-020-0"],
     "ToR2_to_AG2": ["e101-005-0", "e101-006-0", "e101-007-0", "e101-008-0", "e101-021-0", "e101-022-0", "e101-023-0", "e101-024-0"],
     "AG1_to_CR": ["e101-013-0", "e101-014-0", "e101-015-0", "e101-016-0", "e101-029-0", "e101-030-0", "e101-031-0", "e101-032-0"],
     "CR_to_AG2": ["e101-005-0", "e101-006-0", "e101-007-0", "e101-008-0", "e101-021-0", "e101-022-0", "e101-023-0", "e101-024-0"]
}
