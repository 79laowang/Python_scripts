#!/usr/local/bin/python
import pexpect
import sys

ssh_newkey = 'Are you sure you want to continue connecting'
command = 'showmount -e systest1'
child = pexpect.spawn('ssh  root@systest2 "%s"' % command)
i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
fout = file('mylog.txt','w')
if i == 0: #Timeout
    print 'ERROR!'
    print 'SSH could not login. Here is what SSH said:'
    print child.before, child.after
    #return None
if i ==1:
   child.sendline ('yes')
   child.expect ('password: ')
   i = child.expect([pexpect.TIMEOUT, 'password: '])
   if i == 0: # Timeout
       print 'ERROR!'
       print 'SSH could not login. Here is what SSH said:'
       print child.before, child.after
   #    return None˽
child.logfile = fout
#child.logfile = sys.stdout
child.sendline('password')
child.expect(pexpect.EOF)
print child.before
