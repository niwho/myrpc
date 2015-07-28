#coding=utf8
import gevent.monkey
#gevent.monkey.patch_all()
gevent.monkey.patch_all(socket=True, dns=True, time=False, select=True, thread=False, os=True, ssl=True)
from gevent import *
import myrpcframwork
import gevent
import FangJing_pb2
import pkg_resources
import psutil
import thread
import myprotocal
import uuid
import socket
from _socket import error
class myServer(myrpcframwork.Server):
    def __init__(self,listener):
        super(myServer,self).__init__(listener)
    def dispatch(self,uuidstr,pro):
        fj = FangJing_pb2.FangJing()
        while True:
            fj.Clear()
            if len(self.msgqueues[uuidstr])>0:
                #print 'dispatch',self.msgqueues[uuidstr][0]
                if 0x01 == self.msgqueues[uuidstr][0][0]:
                    op = self.msgqueues[uuidstr][0][1]
                    fj.ParseFromString(op)
                    self.posting_machine_state(uuidstr,fj)
                    #print fj.ip,fj.cpu_logic_cores,fj.cpu_userd_per,fj.mem_total,fj.mem_userd_per,fj.net_up,fj.net_down,fj.disk_totoal,fj.disk_used_per
                elif 0x02 == self.msgqueues[uuidstr][0][0]:
                    pro.encodeData(0x02,'')
                self.msgqueues[uuidstr].pop(0)
            else:
                gevent.sleep(1)
    
    def onconnected(self,address,uidstr):
        print 'conected:',address,uidstr
    
    def onclosed(self,address,uidstr): 
        print 'closed:',address,uidstr
    def posting_machine_state(self,uidstr,fj):
        print 'mathcine_state',fj
               
    def handle(self,sock,address):
        #self.onconnected(address)
        print sock,address,'aaaaaa'
        #
        #会话管理
        #
        fileobj = sock.makefile()
        #32字节uuid 128位
        uuid_int_str = fileobj.read(16)
        
        if len(uuid_int_str)!=16:
            print 'err:',len(uuid_int_str)
            self.onclosed(address)
            sock.close()
            #sock.shutdown(socket.SHUT_RDWR)
            return
        else:
            print uuid.UUID(bytes=uuid_int_str)
        #return 
        uuidstr= uuid.UUID(bytes=uuid_int_str).hex
        self.onconnected(address,uuidstr)
        self.msgqueues[uuidstr]=[]
        pro = myprotocal.Protocal2(fileobj)
        glet0 = gevent.spawn(self.dispatch,uuidstr,pro)
        
        while True:
            try:
                msgtype,dat = pro.decodeData()
                #print msgtype
                self.msgqueues[uuidstr].append((msgtype,dat))
            except error:
                #raise
                glet0.kill()
                del self.msgqueues[uuidstr]
                self.onclosed(address,uuidstr)
                break
            except Exception,e:
                print e
                pass
    
class myClient(myrpcframwork.Client):
    def __init__(self):
        super(myClient,self).__init__()
        
        self.fj = FangJing_pb2.FangJing()
        thread.start_new_thread(self.postinginfo,())
        self.pro = myprotocal.Protocal2()
        #gevent.spawn(self.postinginfo)
        
    def handle(self):
        print 'handle'
       # return 
        while True:
            try:
                msgty,dat = self.pro.decodeData()
                #print 'handle',msgty
                if msgty == 0x02:
                    #print 'pong:',msgty
                    pass
                else:
                    self.sync.set(msgty)
                pass
            except error,e:
                sleep(1)
                #print e
            except:
                sleep(1)
                #print 'handle except'
            
    def postinginfo(self):
        ##
        print 'postinginfo'
        ips = ' '.join(socket.gethostbyname_ex(socket.gethostname())[2])
        print ips
       
        while True:
            self.fj.Clear()
            self.fj.ip = ','.join(socket.gethostbyname_ex(socket.gethostname())[2]).strip()#ips.strip()
            net = psutil.net_io_counters()
            net_up = net.bytes_sent
            net_down = net.bytes_recv
            self.fj.cpu_logic_cores = psutil.cpu_count()
            #一秒的间隔
            self.fj.cpu_userd_per = psutil.cpu_percent(1)
            ##
            net = psutil.net_io_counters()
            net_up = net.bytes_sent-net_up
            net_down = net.bytes_recv-net_down
            self.fj.net_up = net_up if net_up>=0 else 4294967296L+net_up
            self.fj.net_down = net_down if net_down>=0 else 4294967296L+net_down
            
            vm = psutil.virtual_memory()
            self.fj.mem_total = vm.total
            self.fj.mem_userd_per = vm.percent
           
            dis = psutil.disk_usage('/')# c盘
            self.fj.disk_totoal = dis.total
            self.fj.disk_used_per = dis.percent
            try:
                self.pro.encodeData(0x01,self.fj.SerializeToString())
            except socket.error:
                gevent.sleep(1)
                #print '++++++++++++++++++++++++++++++++'
            except :
                gevent.sleep(1)
            #self.sock.sendall(self.pro.encodeData(self.fj.SerializeToString()))


            
import sys
import yaml

if __name__ =='__main__':
    #print sys.argv[1]
    if len(sys.argv) > 1:
        svr = myServer(('0.0.0.0',6011))
        svr.serve_forever()
    
    #spawn(postinginfo)
    else:
        print 'client mode'
        cfg = None
        with open('./cfg.yaml') as f:
            cfg = yaml.load(f)
        print cfg
        cli = myClient()
        cli.setserveripp(cfg['client']['ip'],cfg['client']['port'])
    #print cli.func1()
    while True:
        gevent.sleep(1)