########################################################################################################
# Library file
########################################################################################################
from FrameworkLibrary import *
import pexpect
import re
import sys
import time
from   errorsModule import testFailed

class metaswitch_lib :
    #######################################################################################################
    """ Procedure Name: check_cpu
        Description: checks the CPU Utilization and fails if expected value is more than max_cpu
        Parameters Input:
            deviceObjRef = Device object to verify
            max_cpu  =  Maximum expected CPU
    """
    #######################################################################################################
    def check_cpu(self,deviceObjRef,max_cpu):
        self.mydevice = Device.device[deviceObjRef]
        log.info("Check CPU")
        output = self.mydevice.execute("top -bn1", mode="NGOSroot")

        if "Cpu" in output:  # I think it should be load average not Cpu
            match=re.search('Cpu.* ([0-9]+.[0-9]+) id*', output)
            if match:
                #log.info("CPU Usage: %s"%match.group(1))
                cpu = 100 - float(match.group(1))
                if (cpu < max_cpu):
                    log.info("CPU Usage: %s is with in the max_cpu threshold"%cpu)
                else:
                    raise testFailed("CPU usage is more than the max_cpu threshold defined. It is at %s"%cpu)
            else:
                raise testFailed("Could not find idle CPU")
        else:
            raise testFailed("Error in executing CPU usage top command")

    #######################################################################################################
    """ Procedure Name: check_mem
        Description: checks the memory and prints it, no verification done.
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def check_mem(self,deviceObjRef):  #this is just grap memory information????
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("top -bn1", mode="NGOSroot")

        if "KiB Mem" in output:
            match=re.search('KiB Mem:\s+([0-9]+) total,\s+([0-9]+) used,\s+([0-9]+) free,',  output)
            if match:
                log.info("memory Usage: %s %s %s"%(match.group(1),match.group(2),match.group(3)))
            else:
                raise testFailed("Could not find memory output")
        else:
            raise testFailed("Error in executing memory usage for top command")
            log.debug('top command failed')

    #######################################################################################################
    """ Procedure Name: check_bcm_routes
        Description: checks the number of routes in the CAM is matching the routes.
        Parameters Input:
            deviceObjRef = Device object to verify
            routes = expected routes.
    """
    #######################################################################################################
    def check_bcm_routes(self,deviceObjRef,routes):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("hshell -c \"l3 defip show\" | wc", mode="NGOSroot")

        match=re.search('([0-9]+)\s+[0-9]+\s+[0-9]+',  output)
        if match:
            log.info("routes = %s"%match.group(1))
            diff_num = int(routes) - int(match.group(1))
            if ((diff_num >5) or (diff_num <-5)) :
                raise testFailed("Number of BCM routes are: %s, required: %s"%(match.group(1),routes))
            else:
                log.info("Sucess: required routes match")
        else:
            raise testFailed("hshell command failed")

    #######################################################################################################
    """ Procedure Name: check_kernel_routes
        Description: checks the number of routes in the kernel is matching the routes.
        Parameters Input:
            deviceObjRef = Device object to verify
            routes = expected routes.
    """
    #######################################################################################################
    def check_kernel_routes(self,deviceObjRef,routes):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("route -n | wc", mode="NGOSroot")
        output = self.mydevice.execute("ls", mode="NGOSroot")
        output = self.mydevice.execute("route -n | wc", mode="NGOSroot")

        log.info("routes = %s"%output)
        match=re.search('([0-9]+)\s+[0-9]+\s+[0-9]+',  output)
        if match:
            log.info("routes = %s"%match.group(1))
            diff_num = int(routes) - int(match.group(1))
            if ((diff_num >5) or (diff_num <-5)) :
                raise testFailed("Number of kernel routes are: %s, required: %s"%(match.group(1),routes))
            else:
                log.info("Sucess: required kernel routes match")
        else:
            raise testFailed("route command failed")

    #######################################################################################################
    """ Procedure Name: check_vendor_routes
        Description: checks the number of routes in the RIB through vendor CLI is matching the routes.
        Parameters Input:
            deviceObjRef = Device object to verify
            routes = expected routes.
    """
    #######################################################################################################
    def check_vendor_routes(self,deviceObjRef,routes):
        self.mydevice = Device.device[deviceObjRef]

        self.mydevice.execute("nbase_cli", mode="NGOSroot")
        itmp = self.mydevice.execute("show routing | include \"[0-9]+.[0-9]+.[0-9]+.[0-9]+\"| count", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        log.info("vendor inside routes: %s"%itmp)
        match=re.search('Count: ([0-9]+) lines', itmp)
        if match:
            diff_num = int(routes) - int(match.group(1))
            if ((diff_num >5) or (diff_num <-5)) :
                raise testFailed("Number of routes are: %s, required: %s"%(match.group(1),routes))
            else:
                log.info("Sucess: required routes match")
        else:
            raise testFailed("show routing command failed")


    #######################################################################################################
    """ Procedure Name: check_arp
        Description: checks the number of ARP entries
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def check_arp(self,deviceObjRef,arps):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("ip neighbor show | grep REACHABLE | wc", mode="NGOSroot")

        match=re.search('([0-9]+)\s+[0-9]+\s+[0-9]+',  output)
        if match:
            log.info("arps = %s"%match.group(1))
            diff_num = int(arps) - int(match.group(1))
            if ((diff_num >5) or (diff_num <-5)) :
                raise testFailed("Number of ARPs are: %s, required: %s"%(match.group(1),arps))
            else:
                log.info("Sucess: required arps match")
        else:
            raise testFailed("ip neighbor command failed")

    #######################################################################################################
    """ Procedure Name: check_bcm_arp
        Description: checks the number of ARP entries in broadcom
        Parameters Input:
            deviceObjRef = Device object to verify
            routes = expected routes.
    """
    #######################################################################################################
    def check_bcm_arp(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("hshell -c \"l3 egress show\" | wc -l", mode="NGOSroot")

        match=re.search('([0-9]+)\n',  output)
        if match:
            log.info("ARPs = %s"%match.group(1))
        else:
            raise testFailed("hshell command failed")

    #######################################################################################################
    """ Procedure Name: link_shut
        Description: shuts the links of interfaces
        Parameters Input:
            deviceObjRef = Device object to verify
            interfaces = list of interfaces
    """
    #######################################################################################################
    def link_shut(self,deviceObjRef,interfaces):
        self.mydevice = Device.device[deviceObjRef]
        #x=self.mydevice.getInterface("d1_d3_1")

        #log.info("TEST1 %s"%interfaces)
        interfaces = interfaces.strip('[]')
        interfaces = interfaces.replace('\'', '')
        ifaces = interfaces.split(",")

        self.mydevice.execute("nbase_cli", mode="NGOSroot")
        self.mydevice.execute("conf t", mode="NGOSroot")
        for int in ifaces:
            log.info(int)
            #self.mydevice.execute("interface %s"%int, mode="NGOSroot")
            self.mydevice.execute("interface %s disabled"%int, mode="NGOSroot")
            #self.mydevice.execute("disabled", mode="NGOSroot")
            #self.mydevice.execute("commit", mode="NGOSroot")
            #self.mydevice.execute("exit", mode="NGOSroot")

        self.mydevice.execute("commit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        time.sleep(60)

        #for int in ifaces:
            #output = self.mydevice.execute("ifconfig %s"%int, mode="NGOSroot")
#
            #match=re.search('UP BROADCAST RUNNING',  output)
            #if match:
                #raise testFailed("link shut command failed, interface still up")
            #else:
                #log.info("interface is down as expected")
#
    #######################################################################################################
    """ Procedure Name: link_up
        Description: brings up the links of interfaces
        Parameters Input:
            deviceObjRef = Device object to verify
            interfaces = list of interfaces
    """
    #######################################################################################################
    def link_up(self,deviceObjRef,interfaces):
        self.mydevice = Device.device[deviceObjRef]


        interfaces = interfaces.strip('[]')
        interfaces = interfaces.replace('\'', '')
        ifaces = interfaces.split(",")
        #output = self.mydevice.execute("ifup int \n ifconfig int", mode="NGOSroot")

        self.mydevice.execute("nbase_cli", mode="NGOSroot")
        self.mydevice.execute("conf t", mode="NGOSroot")
        for int in ifaces:
            #self.mydevice.execute("interface %s"%int, mode="NGOSroot")
            self.mydevice.execute("interface %s enabled"%int, mode="NGOSroot")
            #self.mydevice.execute("enabled", mode="NGOSroot")
            #self.mydevice.execute("commit", mode="NGOSroot")
            #self.mydevice.execute("exit", mode="NGOSroot")

        self.mydevice.execute("commit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")

        time.sleep(60)
        #for int in ifaces:
            #output = self.mydevice.execute("ifconfig %s"%int, mode="NGOSroot")
            #match=re.search('UP BROADCAST RUNNING',  output)
            #if match:
                #self.mydevice.execute("exit", mode="NGOSroot")
                #log.info("interface is up")
            #else:
                #self.mydevice.execute("exit", mode="NGOSroot")
                #raise testFailed("link up command failed, interface still down")


    #######################################################################################################
    """ Procedure Name: check_ospf_neighbors
        Description: checks the OSPF neighbors matching
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def check_ospf_neighbors(self,deviceObjRef,neighbors):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("nbase_cli", mode="NGOSroot")
        output = self.mydevice.execute("show ospfv2 neighbor | include FULL | count", mode="NGOSroot")

        self.mydevice.execute("exit", mode="NGOSroot")
        match=re.search('Count: ([0-9]+) lines',  output) # + which means it is possible more than single digit can be exist
        if match:
            if  (int(match.group(1)) != int(neighbors)) :
                raise testFailed("Number of OSPF neighbors are: %s, required: %s"%(match.group(1),neighbors))
            log.info("success")
        else:
            raise testFailed("ospf show command failed")


    #######################################################################################################
    """ Procedure Name: check_bgp_neighbors
        Description: checks the OSPF neighbors matching
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def check_bgp_neighbors(self,deviceObjRef,asn,neighbors):
        self.mydevice = Device.device[deviceObjRef]
        #strtosend='show bgp ' + asn + ' neighbor-state-list | include \"state                       established\" |  count'
        strtosend='show bgp ' + asn + ' neighbor-state-list | include \" state\" | include established | count'
        self.mydevice.execute("nbase_cli", mode="NGOSroot")
        output = self.mydevice.execute(strtosend, mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")

        match=re.search('Count: ([0-9]+) lines',  output)
        if match:
            if  (int(match.group(1)) != int(neighbors)) :
                raise testFailed("Number of BGP neighbors are: %s, required: %s"%(match.group(1),neighbors))
            log.info("success")
        else:
            raise testFailed("bgp show command failed")


    #######################################################################################################
    """ Procedure Name: upgrade_vendor_packages
        Description: upgrades the pacakges
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def upgrade_vendor_packages(self,deviceObjRef,abort):
        self.mydevice = Device.device[deviceObjRef]
        self.mydevice.execute("dpkg --remove ymmconfd confd-basic nst-eval", mode="NGOSroot")
        self.mydevice.execute("cd /var/opt/metaswitch/confd/cdb", mode="NGOSroot")
        self.mydevice.execute("rm *.cdb", mode="NGOSroot")
        self.mydevice.execute("cd /home/admin", mode="NGOSroot")
        self.mydevice.execute("tar -xsvf nst-eval-install.tar.gz ", mode="NGOSroot")
        self.mydevice.execute("cd nst-eval-install", mode="NGOSroot")

        #log.info("Abort %s"%abort)
        if int(abort):
            self.mydevice.transmit('dpkg -i ./*.deb')
            self.mydevice.receive('.*')
            time.sleep(4)
            self.mydevice.transmit('\x03')
            self.mydevice.receive('.*OPX')
        else:
            output= self.mydevice.execute("dpkg -i ./*.deb", mode="NGOSroot")
            output = self.mydevice.execute("apt-get -f -y --force-yes install", mode="NGOSroot")

            match=re.search('Error',  output)
            if match:
                raise testFailed("Installation failed")
            else:
                log.info("installation success")
            #output = self.mydevice.execute("apt-get -f -y --force-yes install", mode="NGOSroot")

    #######################################################################################################
    """ Procedure Name: uninstall_vendor_packages
        Description: uninstall the packages
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################

    def uninstall_vendor_packages(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]

        output = self.mydevice.execute("dpkg --remove ymmconfd confd-basic nst-eval", mode="NGOSroot")
        self.mydevice.execute("cd /var/opt/metaswitch/confd/cdb", mode="NGOSroot")
        self.mydevice.execute("rm *.cdb", mode="NGOSroot")

        match=re.search('Error',  output)
        if match:
            raise testFailed("Installation failed")
        else:
            log.info("installation success")

    #######################################################################################################
    """ Procedure Name: clean_install_vendor_packages
        Description: Clean install pacakges
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def clean_install_vendor_packages(self,deviceObjRef,abort):
        self.mydevice = Device.device[deviceObjRef]
        self.mydevice.execute("cd /home/admin", mode="NGOSroot")
        self.mydevice.execute("tar -xsvf nst-eval-install.tar.gz ", mode="NGOSroot")
        self.mydevice.execute("tar -xsvf nst-eval-install_1.0.2.tar.gz ", mode="NGOSroot")
        self.mydevice.execute("cd nst-eval-install", mode="NGOSroot")
# int 0 means false and int non zero is true in python, so the abort = 1 it should got o if, if abort = 0, it will go to else.
        #log.info("Abort: %s"%abort)
        if int(abort):
            self.mydevice.transmit('dpkg -i ./*.deb')
            self.mydevice.receive('.*')
            time.sleep(2)
            self.mydevice.transmit('\x03')   # send ctrl c
            self.mydevice.receive('.*OPX')
        else:
            output= self.mydevice.execute("dpkg -i ./*.deb", mode="NGOSroot")
            output = self.mydevice.execute("apt-get -f -y --force-yes install", mode="NGOSroot")
            match=re.search('Error',  output)
            if match:
                raise testFailed("Installation failed")
            else:
                log.info("installation success")


    #######################################################################################################
    """ Procedure Name: verify_vendor_processes
        Description: check if all the vendor processes are up and running
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def verify_vendor_processes(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("systemctl status confd", mode="NGOSroot")

        match=re.search('active \(running\)',  output)
        if match:
            log.info("success")
        else:
            raise testFailed("confd is not running")

        output = self.mydevice.execute("systemctl status ymm", mode="NGOSroot")
        match=re.search('active \(running\)',  output)
        if match:
            log.info("success")
        else:
            raise testFailed("ymm is not running")

        output = self.mydevice.execute("systemctl status pymm", mode="NGOSroot")
        match=re.search('active \(running\)',  output)
        if match:
            log.info("success")
        else:
            raise testFailed("ymm is not running")


        output = self.mydevice.execute("systemctl status nbased", mode="NGOSroot")
        match=re.search('active \(running\)',  output)
        if match:
            log.info("success")
        else:
            raise testFailed("nbased is not running")

    #######################################################################################################
    """ Procedure Name: Reboots the switch
        Description: Reboot the switch
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def switch_reboot(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.reload(timeout=600)
        time.sleep(900)

    def connect_ssh(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.connect(protocol='ssh', portType='mgmtIp')

    def check_interface_statistics(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("ifconfig -a | grep errors", mode="NGOSroot")
        match=re.search('errors: ([0-9]+)', output)
        if match:
            log.info("success")
        else:
            raise testFailed("ifconfig error")

    def verify_eval_license(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("openssl x509 -in /etc/opt/metaswitch/license -text -noout | grep \"Not After\"", mode="NGOSroot")
        match=re.search('errors: ([0-9]+)', output)
        #curr_date=datetime.datetime.now()


    #######################################################################################################
    """ Procedure Name:  Remove vendor files
        Description: Remove the nbased file
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def remove_vendor_files(self,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]
        output = self.mydevice.execute("rm -f /opt/metaswitch/bin/nbased", mode="NGOSroot")

    def load_cfg(self,cfg,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]

        self.mydevice.execute("nbase_cli", mode="NGOSroot")  #what is mean of NGOSroot ?
        self.mydevice.execute("conf t", mode="NGOSroot")
        self.mydevice.execute("load replace "+cfg, mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")
        self.mydevice.execute("exit", mode="NGOSroot")

    def copy_file_to_switch(self,src,dst,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]  # Need understand why Device.device ??

        #issue with metaswitch
        #Change the owner to admin for /home/admin, ownership is changed to root after installing metaswitch packages
        self.mydevice.execute("chown admin /home/admin", mode="NGOSroot")
        self.mydevice.execute("rm -f /home/admin/"+dst, mode="NGOSroot")  # Need understand how dst can point to {MSW_PKG_DST}
        #Why not using {MSW_PKG_DST} instead of dst
        ip = self.mydevice.get('managementIP')  #which case look which file ? this case, it look up mataswitch.yaml file
        log.info(ip)   # what is this for ?

        sw = pexpect.spawn ('/usr/bin/scp ' + src + ' admin@'+ip+':'+dst)  #src look up the l3 robot.file and why not define {MSW_PKG_SRC} ?, This command is running under EQX-03 not DUT
        sw.logfile = sys.stdout
        #i = sw.expect('.*password:')
        i = sw.expect([r'.*\?', r'.*password:', pexpect.EOF, pexpect.TIMEOUT])   # what is mean of r here ?, Need try with ssh-kevin.py
        #log.info("src=%s, dst=%s"%(src,dst))
        log.info(sw.after)
        if i==0:
            sw.sendline('yes\r')
            sw.expect('.*password:');
            log.info(sw.after)
            sw.sendline('admin');
            sw.expect('100')
            log.info(sw.after) # why 2 times ?

        elif i==1:
            sw.sendline('admin');
            sw.expect('100')      #This means 100% complete scp file transfer
            log.info(sw.after)
        elif i==2:
            log.info('EOF:')
            log.info(sw.after)
        else:
            log.info('timeout')
            log.info(sw.after)

        sw.close()

    #output = self.mydevice.execute("rm -f /opt/metaswitch/bin/nbased", mode="NGOSroot")

    #######################################################################################################
    """ Procedure Name:  Verify Perpetual License
        Description: Verifies installing perpetual license
        Parameters Input:
            deviceObjRef = Device object to verify
    """
    #######################################################################################################
    def verify_perpetual_license(self,lic,deviceObjRef):
        self.mydevice = Device.device[deviceObjRef]

        output = self.mydevice.execute("openssl x509 -in /etc/opt/metaswitch/license -text -noout | grep \"Not After\"", mode="NGOSroot")
        match=re.search('Not After : Dec 31 23:59:59 9999',  output)
        if match:
            log.info("Perpetual license is already installed, nothing else to do")
            return
        self.mydevice.execute("systemctl restart nbased", mode="NGOSroot")

        cmd = "cp -f /home/admin/" + lic + " /etc/opt/metaswitch/license"
        self.mydevice.execute(cmd, mode="NGOSroot")
        self.mydevice.execute("systemctl restart nbased", mode="NGOSroot")

        output = self.mydevice.execute("systemctl status nbased", mode="NGOSroot")
        match=re.search('active \(running\)',  output)
        if match:
            log.info("success")
        else:
            raise testFailed("nbased is not running")

        output = self.mydevice.execute("openssl x509 -in /etc/opt/metaswitch/license -text -noout | grep \"Not After\"", mode="NGOSroot")
        match=re.search('Not After : Dec 31 23:59:59 9999',  output)
        if match:
            log.info("success")
        else:
            raise testFailed("Did not get the exepected license dutation")
