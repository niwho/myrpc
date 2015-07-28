#coding=utf8
import struct

class Protocal1(object):
    def __init__(self,f=None):
        self.fileobj = f
    
    def setfileobj(self,f):
        self.fileobj = f    
        
    def parseHeader(self):
        d = self.fileobj.read(1)
        if len(d)==0:
            raise
        d, = struct.unpack('!B',d)
        
        if d&0x01:
            return 1
        elif d&0x02:
            return 2
        elif d&0x04:
            return 4
        elif d&0x10:
            return 8
        elif d&0x20:
            return 16
        else:
            return d
    
    def makeHeader(self,op):
        d = struct.pack('!B',op)
        self.fileobj.write(d)
        self.fileobj.flush()
        
        
class Protocal2(object):
    def __init__(self,f=None):
        self.fileobj = f
    
    def setfileobj(self,f):
        self.fileobj = f     
    
    #000 前4个字节保留  0000 类型  00000000 长度  00000.... 数据
    #类型 0x1 protobuf
    def encodeData(self,msgty,date):
        firstbyte = msgty
        secondbyte = len(date)
        dat = struct.pack('!BB',firstbyte,secondbyte)+str(date)
        self.fileobj.write(dat)
        self.fileobj.flush()
        
    def decodeData(self):
        f_s = self.fileobj.read(2)
        if len(f_s) != 2:
            #print 'data:',data
            raise Exception('socket err')
        fi,se = struct.unpack('!BB',f_s)
        if fi == 0x1:
            dat = self.fileobj.read(se)
            if len(dat) != se:
                raise Exception('socket err')
            return 0x1,dat
        elif fi == 0x2:
            return 0x2,''
        
        
        
        
    