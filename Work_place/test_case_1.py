from FrameworkLibrary import *
import pexpect
import re
import sys
import time
from   errorsModule import testFailed

def copy_file_to_switch(self,src,dst,deviceObjRef):
      self.mydevice = Device.device[deviceObjRef]  # Need understand why Device.device ??

      #issue with metaswitch
      #Change the owner to admin for /home/admin, ownership is changed to root after installing metaswitch packages
      self.mydevice.execute("chown admin /home/admin", mode="NGOSroot")
      self.mydevice.execute("rm -f /home/admin/"+dst, mode="NGOSroot")  # Need understand how dst can point to {MSW_PKG_DST}
      #Why not using {MSW_PKG_DST} instead of dst
      ip = self.mydevice.get('managementIP')  #which case look which file ? this case, it look up mataswitch.yaml file
      log.info(ip)   # what is this for ?

      sw = pexpect.spawn ('/usr/bin/scp ' + src + ' admin@'+ip+':'+dst)  #src look up the l3 robot.file and why not define {MSW_PKG_SRC} ?
      sw.logfile = sys.stdout
      #i = sw.expect('.*password:')
      i = sw.expect([r'.*\?', r'.*password:', pexpect.EOF, pexpect.TIMEOUT])   # what is mean of r here ?
      #log.info("src=%s, dst=%s"%(src,dst))
      log.info(sw.after)
      if i==0:
          sw.sendline('yes\r')
          sw.expect('.*password:');
          log.info(sw.after)   # what is this ?
          sw.sendline('admin');
          sw.expect('100')
          log.info(sw.after)

      elif i==1:
          sw.sendline('admin');
          sw.expect('100')      #what is this ?
          log.info(sw.after)
      elif i==2:
          log.info('EOF:')
          log.info(sw.after)
      else:
          log.info('timeout')
          log.info(sw.after)

      sw.close()

def main():
    
