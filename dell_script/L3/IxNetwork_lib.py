import getpass
import sys
import telnetlib
import time
import re
import pexpect
import os
import IxNetwork
from FrameworkLibrary import *

class IxNetwork_lib :
    def load_ixnetwork_cfg(self,ixChassis,ixTclServer,ixTclPort,ConfigFile) :

        ixNet = IxNetwork.IxNet()
        print 'Verifying ixNetwork.IxNet() :',ixNet
        
        getNull = ixNet.getNull()
        print 'Verifying ixNet.getNull() :',getNull
        
        #log.info("check value : %s"%ixTclPort)

        connect = ixNet.connect(ixTclServer,'-port',ixTclPort,'-version','7.31')
        print 'Verifying ixNet.connect() :',connect
        
        getVersion = ixNet.getVersion()
        print 'Verifying ixNet.getVersion():',getVersion
        
        setSessionParameter = ixNet.setSessionParameter('setAttr','strict')
        print 'Verifying ixNet.setSessionParameter() :',setSessionParameter

        # clear the configuration
        ixNet.execute('newConfig')
        root = ixNet.getRoot()
        print 'ixNet root:', root
        ##ixNet.help(*args)
        helpRoot = ixNet.help(root)
        helpRoot = ixNet.help(root)
        print 'Verifying ixNet.help(vport1) :',helpRoot
        # This will load the ixNetwork configuration file    
        readFrom = ixNet.execute('loadConfig',ixNet.readFrom(ConfigFile))
        #,'-ixNetRelative')
        print 'Verifying ixNet.readFrom() :',readFrom
        
        # add chassis
        #chassis = ixNet.add(ixNet.getRoot()+'availableHardware', 'chassis', '-hostname', ixChassis)
        #ixNet.commit()
        
        timeInSeconds = 60
        time.sleep(timeInSeconds)

        print 'Starting Protocols'
        readFrom=ixNet.execute('startAllProtocols')
        print 'Verifying ixNet.readFrom() :',readFrom
