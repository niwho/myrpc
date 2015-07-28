#coding=utf8

import gevent
from gevent import monkey 
from _socket import error
#monkey.patch_all()
gevent.monkey.patch_all(socket=True, dns=True, time=False, select=True, thread=False, os=True, ssl=True)
from gevent import *
from gevent.event import *
import sys
import _socket
from gevent.socket import EWOULDBLOCK, socket
import struct
import uuid
import myprotocal
#import socket as _socket

def _tcp_listener(address, backlog=50, reuse_addr=None, family=_socket.AF_INET):
    """A shortcut to create a TCP socket, bind it and put it into listening state."""
    sock = socket(family=family)
    if reuse_addr is not None:
        sock.setsockopt(_socket.SOL_SOCKET, _socket.SO_REUSEADDR, reuse_addr)
    try:
        sock.bind(address)
    except _socket.error:
        ex = sys.exc_info()[1]
        strerror = getattr(ex, 'strerror', None)
        if strerror is not None:
            ex.strerror = strerror + ': ' + repr(address)
        raise
    sock.listen(backlog)
    sock.setblocking(0)
    return sock

def _parse_address(address):
    if isinstance(address, tuple):
        if ':' in address[0]:
            return _socket.AF_INET6, address
        return _socket.AF_INET, address
    elif isinstance(address, string_types):
        if ':' in address:
            host, port = address.rsplit(':', 1)
            family, host = _extract_family(host)
            if host == '*':
                host = ''
            return family, (host, int(port))
        else:
            return _socket.AF_INET, ('', int(address))
    elif isinstance(address, integer_types):
        return _socket.AF_INET, ('', int(address))
    else:
        raise TypeError('Expected tuple or string, got %s' % type(address))


def parse_address(address):
    try:
        return _parse_address(address)
    except ValueError:
        raise ValueError('Failed to parse address %r: %s' % (address, sys.exc_info()[1]))
if sys.platform == 'win32':
    # SO_REUSEADDR on Windows does not mean the same thing as on *nix (issue #217)
    DEFAULT_REUSE_ADDR = None
else:
    DEFAULT_REUSE_ADDR = 1
    
class Server(object):
    
    # the number of seconds to sleep in case there was an error in accept() call
    # for consecutive errors the delay will double until it reaches max_delay
    # when accept() finally succeeds the delay will be reset to min_delay again
    min_delay = 0.01
    max_delay = 1

    # Sets the maximum number of consecutive accepts that a process may perform on
    # a single wake up. High values give higher priority to high connection rates,
    # while lower values give higher priority to already established connections.
    # Default is 100. Note, that in case of multiple working processes on the same
    # listening value, it should be set to a lower value. (pywsgi.WSGIServer sets it
    # to 1 when environ["wsgi.multiprocess"] is true)
    max_accept = 100
    backlog = 256
    reuse_addr = DEFAULT_REUSE_ADDR
    _spawn = Greenlet.spawn
    
    def __init__(self, listener, backlog=None, spawn='default', **ssl_args):
        
        self.msgqueues={}
        
        self._stop_event = Event()
        self._stop_event.set()
        self._watcher = None
        self._timer = None
        self.pool = None
        
        self.loop = get_hub().loop
        try:
            if ssl_args:
                ssl_args.setdefault('server_side', True)
                from gevent.ssl import wrap_socket
                self.wrap_socket = wrap_socket
                self.ssl_args = ssl_args
            else:
                self.ssl_args = None
            if backlog is not None:
                if hasattr(self, 'socket'):
                    raise TypeError('backlog must be None when a socket instance is passed')
                self.backlog = backlog
            
            self.family, self.address = parse_address(listener)
        except:
            self.close()
            raise
        pass
    def start_accepting(self):
        if self._watcher is None:
            # just stop watcher without creating a new one?
            self._watcher = self.loop.io(self.socket.fileno(), 1)
            self._watcher.start(self._do_read)
    def do_read(self):
        try:
            client_socket, address = self.socket.accept()
        except _socket.error, err:
            if err[0] == EWOULDBLOCK:
                return
            raise
        return socket(_sock=client_socket), address        
    def full(self):
        return False
    def _do_read(self):
        for _ in xrange(self.max_accept):
            if self.full():
                self.stop_accepting()
                return
            try:
                args = self.do_read()
                self.delay = self.min_delay
                if not args:
                    return
            except:
                self.loop.handle_error(self, *sys.exc_info())
                ex = sys.exc_info()[1]
                if self.is_fatal_error(ex):
                    self.close()
                    sys.stderr.write('ERROR: %s failed with %s\n' % (self, str(ex) or repr(ex)))
                    return
                if self.delay >= 0:
                    self.stop_accepting()
                    self._timer = self.loop.timer(self.delay)
                    self._timer.start(self._start_accepting_if_started)
                    self.delay = min(self.max_delay, self.delay * 2)
                break
            else:
                try:
                    self.do_handle(*args)
                except:
                    self.loop.handle_error((args[1:], self), *sys.exc_info())
                    if self.delay >= 0:
                        self.stop_accepting()
                        self._timer = self.loop.timer(self.delay)
                        self._timer.start(self._start_accepting_if_started)
                        self.delay = min(self.max_delay, self.delay * 2)
                    break
    def do_handle(self, *args):
        spawn = self._spawn
        if spawn is None:
            self._handle(*args)
        else:
            spawn(self._handle, *args)
    def wrap_socket_and_handle(self, client_socket, address):
        # used in case of ssl sockets
        ssl_socket = self.wrap_socket(client_socket, **self.ssl_args)
        return self.handle(ssl_socket, address)
    
    @classmethod
    def get_listener(self, address, backlog=None, family=None):
        if backlog is None:
            backlog = self.backlog
        return _tcp_listener(address, backlog=backlog, reuse_addr=self.reuse_addr, family=family)
    
    def init_socket(self):
        if not hasattr(self, 'socket'):
            self.socket = self.get_listener(self.address, self.backlog, self.family)
            self.address = self.socket.getsockname()
        if self.ssl_args:
            self._handle = self.wrap_socket_and_handle
        else:
            self._handle = self.handle
    
    def start(self):
        """Start accepting the connections.

        If an address was provided in the constructor, then also create a socket,
        bind it and put it into the listening mode.
        """
        self.init_socket()
        self._stop_event.clear()
        try:
            self.start_accepting()
        except:
            self.close()
            raise
    def stop_accepting(self):
        if self._watcher is not None:
            self._watcher.stop()
            self._watcher = None
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
    def close(self):
        """Close the listener socket and stop accepting."""
        self._stop_event.set()
        try:
            self.stop_accepting()
        finally:
            try:
                self.socket.close()
            except Exception:
                pass
            finally:
                self.__dict__.pop('socket', None)
                self.__dict__.pop('handle', None)
                self.__dict__.pop('_handle', None)
                self.__dict__.pop('_spawn', None)
                self.__dict__.pop('full', None)
                if self.pool is not None:
                    self.pool._semaphore.unlink(self._start_accepting_if_started)

    def stop(self, timeout=None):
        """Stop accepting the connections and close the listening socket.

        If the server uses a pool to spawn the requests, then :meth:`stop` also waits
        for all the handlers to exit. If there are still handlers executing after *timeout*
        has expired (default 1 second), then the currently running handlers in the pool are killed."""
        self.close()
        if timeout is None:
            timeout = self.stop_timeout
        if self.pool:
            self.pool.join(timeout=timeout)
            self.pool.kill(block=True, timeout=1)
    @property
    def started(self):
        return not self._stop_event.is_set()
    
    def serve_forever(self, stop_timeout=None):
        """Start the server if it hasn't been already started and wait until it's stopped."""
        # add test that serve_forever exists on stop()
        if not self.started:
            self.start()
        try:
            self._stop_event.wait()
        finally:
            Greenlet.spawn(self.stop, timeout=stop_timeout).join()
    def run(self):
        if not self.started:
            self.start()
    def func1(self,f):
        print 'func1'
        f.write(struct.pack("!B",0x1))  
        f.flush() 
    def func2(self,f):
        print 'func2'
        f.write(struct.pack("!B",0x2))  
        f.flush()    
    def dispatch(self,uuidstr):
        while True:
            if len(self.msgqueues[uuidstr])>0:
                op = self.msgqueues[uuidstr][0]
                if op == 1:
                    self.func1(self.fileobj)
                elif op == 2:
                    self.func2(self.fileobj)
                else:
                    self.fileobj.write(struct.pack("!B",0x80))  
                    self.fileobj.flush()
                    #print 'ignore:',op
                # no eception
                self.msgqueues[uuidstr].pop(0)
            else:
                sleep(1)
                
    def handle(self,sock,address):
        print sock,address
        #
        #会话管理
        #
        self.fileobj = sock.makefile()
        fileobj = self.fileobj
        #32字节uuid 128位
        uuid_int_str = fileobj.read(16)
        
        if len(uuid_int_str)!=16:
            print 'err:',len(uuid_int_str)
            sock.close()
            return 
        else:
            print uuid.UUID(bytes=uuid_int_str)
        #return 
        uuidstr= uuid.UUID(bytes=uuid_int_str).hex
        if uuidstr not in self.msgqueues:
            self.msgqueues[uuidstr]=[]
        pro = myprotocal.Protocal2(fileobj)
        gevent.spawn(self.dispatch,uuidstr)
        
        while True:
            try:
                dat = pro.decodeData()
                self.msgqueues[uuidstr].append(dat)
            except error:
                #raise
                sock.close()
                break
            except Exception,e:
                print e
                pass
            continue
            
            line = fileobj.readline()
            if not line:
                print("client disconnected")
                break
            if line.strip().lower() == 'quit':
                print("client quit")
                break
            fileobj.write(line)
            fileobj.flush()
            print("echoed %r" % line)
            
class Client(object):
    def __init__(self):
        self.isalive = False
        self.pro = myprotocal.Protocal1()
        self.sync = gevent.event.AsyncResult()
    
    def setserveripp(self,ip,port):
        self.ipp = (ip,port)
        self.uuidstr = uuid.uuid1().bytes
        self.sock = socket(_socket.AF_INET, _socket.SOCK_STREAM)
        try:
            self.sock.connect(self.ipp)
            self.sock.sendall(self.uuidstr)
            self.pro.setfileobj(self.sock.makefile())
        except error:
            pass
        gevent.spawn(self.handle)
        gevent.spawn(self.keep_alive)
        
    def postinginfo(self):
        pass
    
    def handle(self):
        print 'handle'
        return 
        while True:
            try:
                msgty,dat = self.pro.parseHeader()
                #print 'handle',rt
                if msgty == 0x20:
                    print 'pong:',msgty
                    pass
                else:
                    self.sync.set(msgty)
                pass
            except error:
                print 'hhhhhhhh'
                sleep(0.1)
            except:
                pass
    def keep_alive(self):
        print 'keep_alive'
        #心跳包
        #heartbeat_pkt=struct.pack('!B',0x80)
        while True:
            #每隔4s 发送一次心跳
            sleep(4)
            try:
                #self.sock.sendall(heartbeat_pkt)
                self.pro.encodeData(0x02,'')
                pass
            #except error:
            except:
                #尝试重连
                self.isalive = False
                self.sock = socket(_socket.AF_INET, _socket.SOCK_STREAM)
                while not self.isalive:
                    try:
                        self.sock.connect(self.ipp)
                        self.sock.sendall(self.uuidstr)
                        self.pro.setfileobj(self.sock.makefile())
                        
                        self.isalive = True
                    except error,e:
                        #print e
                        self.sock = socket(_socket.AF_INET, _socket.SOCK_STREAM)
                        self.isalive = False
                        #print 'kkkkk'
                        sleep(1)
                    except:
                        print '2k2k2k2k2'
                        sleep(1)
                        
    
    def call_method(self):
        pass
    def func1(self):
        self.pro.makeHeader(0x01)
        return self.sync.get()
    
    

        
if __name__=='__main__':
    if sys.argv[1] == 0:
        svr = Server(('0.0.0.0',6011))
        svr.serve_forever()
    else:
        pass
    #import signal
    #gevent.signal(signal.SIG_DFL  , gevent.kill)
    #thread = gevent.spawn(svr.run_forever)
    #thread.join()