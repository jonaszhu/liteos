#! /usr/bin/env python
import threading
import os
import sys
import subprocess
import time
import subprocess

#20 and 29 removed

commtable = [8, 10, 12, 16, 18]
startid = 1
commonchannel = 21

class MyThread ( threading.Thread ):

    def __init__ ( self, port, nodeid, channel, networkname, nodename ):
        self.port = port
        self.nodeid = nodeid
        self.channel = channel
        self.networkname = networkname
        self.nodename = nodename
        threading.Thread.__init__ ( self )

    def run ( self ):

        cmdtemp = 'java tools.installer.installer ' + self.port +' '+ 'MIB520'+ ' '+ self.nodeid + ' '+ self.channel+ ' LiteOS.hex ' + self.networkname+ ' '+ self.nodename +' &' 
        print 'For node '+self.nodeid+ ' the string is '+ cmdtemp
        #subprocess.Popen(["/bin/ls","/"], stdout=subprocess.PIPE)
        #subprocess.Popen([cmdtemp, cmdtemp2], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        #fout = os.popen(cmdtemp)
        #resultoutput = fout.read()
        #print resultoutput
        
for i in range(1, 5):
    commport = 'COM'+str(commtable[i-1])
    print 'Hello'
    cmdtemp = 'java tools.installer.installer ' + commport +' '+ 'MIB520'+ ' '+ str(startid+i-1) + ' '+  str(commonchannel)+ ' LiteOS.hex ' + 'ssn01'+ ' '+ 'node'+str(startid+i-1) 
    print cmdtemp
    p = subprocess.Popen([sys.executable, cmdtemp], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)

    #fout=os.popen(cmdtemp)
    #resultoutput=fout.read()
    #print resultoutput
    #MyThread(commport, str(startid+i-1), str(commonchannel), 'ssn01', 'node'+str(startid+i-1) ).start()
    #time.sleep(1)