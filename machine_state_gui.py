# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from FangJing_pb2 import FangJing

###########################################################################
## Class MyFrame1
###########################################################################
class MyPanel2(wx.Panel):
    def __init__(self,parent):
        super(MyPanel2,self).__init__(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        #self.m_panel1 = #wx.Panel( parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        m_wrap_sizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_node = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_node.Wrap( -1 )
        m_wrap_sizer.Add( self.m_node, 1, wx.ALL, 5 )
        
        m_outer_sizer4 = wx.BoxSizer( wx.VERTICAL )
        
        m_inner_sizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_item_lable4 = wx.StaticText( self, wx.ID_ANY, u"CPU", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_item_lable4.Wrap( -1 )
        m_inner_sizer4.Add( self.m_item_lable4, 0, wx.ALL, 5 )
        
        self.m_gauge4 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge4.SetValue( 0 ) 
        m_inner_sizer4.Add( self.m_gauge4, 0, wx.ALL, 5 )
        
        
        m_outer_sizer4.Add( m_inner_sizer4, 0, wx.EXPAND, 5 )
        
        self.m_data_panel4 = wx.StaticText( self, wx.ID_ANY, u"data", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_data_panel4.Wrap( -1 )
        m_outer_sizer4.Add( self.m_data_panel4, 0, wx.ALL, 5 )
        
        
        m_wrap_sizer.Add( m_outer_sizer4, 1, wx.EXPAND, 5 )
        
        m_outer_sizer1 = wx.BoxSizer( wx.VERTICAL )
        
        m_inner_sizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_item_lable1 = wx.StaticText( self, wx.ID_ANY, u"MEM", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_item_lable1.Wrap( -1 )
        m_inner_sizer1.Add( self.m_item_lable1, 0, wx.ALL, 5 )
        
        self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 ) 
        m_inner_sizer1.Add( self.m_gauge1, 0, wx.ALL, 5 )
        
        
        m_outer_sizer1.Add( m_inner_sizer1, 0, wx.EXPAND, 5 )
        
        self.m_data_panel1 = wx.StaticText( self, wx.ID_ANY, u"data", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_data_panel1.Wrap( -1 )
        m_outer_sizer1.Add( self.m_data_panel1, 0, wx.ALL, 5 )
        
        
        m_wrap_sizer.Add( m_outer_sizer1, 1, wx.EXPAND, 5 )
        
        m_outer_sizer2 = wx.BoxSizer( wx.VERTICAL )
        
        m_inner_sizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_item_lable2 = wx.StaticText( self, wx.ID_ANY, u"NET", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_item_lable2.Wrap( -1 )
        m_inner_sizer2.Add( self.m_item_lable2, 0, wx.ALL, 5 )
        
        self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 ) 
        m_inner_sizer2.Add( self.m_gauge2, 0, wx.ALL, 5 )
        
        
        m_outer_sizer2.Add( m_inner_sizer2, 0, wx.EXPAND, 5 )
        
        self.m_data_panel2 = wx.StaticText( self, wx.ID_ANY, u"data", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_data_panel2.Wrap( -1 )
        m_outer_sizer2.Add( self.m_data_panel2, 0, wx.ALL, 5 )
        
        
        m_wrap_sizer.Add( m_outer_sizer2, 1, wx.EXPAND, 5 )
        
        m_outer_sizer3 = wx.BoxSizer( wx.VERTICAL )
        
        m_inner_sizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_item_lable3 = wx.StaticText( self, wx.ID_ANY, u"DISK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_item_lable3.Wrap( -1 )
        m_inner_sizer3.Add( self.m_item_lable3, 0, wx.ALL, 5 )
        
        self.m_gauge3 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge3.SetValue( 0 ) 
        m_inner_sizer3.Add( self.m_gauge3, 0, wx.ALL, 5 )
        
        
        m_outer_sizer3.Add( m_inner_sizer3, 0, wx.EXPAND, 5 )
        
        self.m_data_panel3 = wx.StaticText( self, wx.ID_ANY, u"data", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_data_panel3.Wrap( -1 )
        m_outer_sizer3.Add( self.m_data_panel3, 0, wx.ALL, 5 )
        
        
        m_wrap_sizer.Add( m_outer_sizer3, 1, wx.EXPAND, 5 )
        
        
        bSizer3.Add( m_wrap_sizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer3 )
        self.Layout()
        bSizer3.Fit( self)   
        
        self.o1 = 0
        self.o2 = 0
        self.o3 = ''
        
    def update(self,fj):
        if self.o3 != fj.ip:
            self.o3 = fj.ip
            self.m_node.SetLabel(fj.ip)
        self.m_data_panel4.SetLabel(u'逻辑核数:%d,使用率:%d%%'%(fj.cpu_logic_cores,fj.cpu_userd_per))
        self.m_gauge4.SetValue(fj.cpu_userd_per)
        
        self.m_data_panel1.SetLabel(u'内存总量:%dMB,已用:%d%%'%(fj.mem_total/1024,fj.mem_userd_per))
        if self.o1 !=int(fj.mem_userd_per):
            print 'o1',fj.mem_userd_per
            self.o1 = int(fj.mem_userd_per)
            self.m_gauge1.SetValue(fj.mem_userd_per)
        
        self.m_data_panel2.SetLabel(u'上行:%dKB/s,下行:%dKB/s'%(fj.net_up/1024,fj.net_down/1024))
        
        self.m_data_panel3.SetLabel(u'C盘总量:%dGB,已用:%d%%'%(fj.disk_totoal/1024/1024,fj.disk_used_per))
        if self.o2 != int(fj.disk_used_per):
            self.o2 = int(fj.disk_used_per)
            print 'o2',self.o2
            self.m_gauge3.SetValue(fj.disk_used_per)
   
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1350,340), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
        self.icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        
        self.panels={}
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.SetSizer( self.bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        ##########
        self.Bind( wx.EVT_CLOSE, self.MyFrame1OnClose )
        self.Bind(EVT_REMOVE, self.removePanel)
        self.Bind(EVT_ADD, self.addPanel)
        self.Bind(EVT_UPDATE, self.updatePanel)
        
        ######
        #thread.start_new_thread(self.addPanel,('uuidstr',))
        #self.addPanel('uuidstr')
        self.bSizer1.Layout()
        self.Fit()
        #self.bSizer1.Add( MyPanel2(self), 1, wx.EXPAND |wx.ALL, 0 )
        #print self.bSizer1.Children
    def addPanel(self,evt):
        #print 'addPanel'
        uuidstr = evt.GetValue()
        self.panels[uuidstr] = MyPanel2(self)
        self.bSizer1.Add( self.panels[uuidstr], 1, wx.EXPAND |wx.ALL, 0 )
        self.Layout()
        self.Fit()
        #self.Refresh()
    
    def removePanel(self,evt):
        print 'removePanel'
        uuidstr = evt.GetValue()
        self.bSizer1.Detach(self.panels[uuidstr])
        self.panels[uuidstr].Destroy()
        del self.panels[uuidstr]
        self.Layout()
        self.Fit()
        #self.Refresh()
    
    def updatePanel(self,evt):
        uuidstr,fj = evt.GetValue()
        print uuidstr,type(fj),fj
        self.panels[uuidstr].update(fj)
    def updatePanel2(self,uuidstr,fj):
        #uuidstr,fj = evt.GetValue()
        self.panels[uuidstr].update(fj)    
    def MyFrame1OnClose( self, event ):
        #event.Skip()
        print 'MyFrame1OnClose'
        wx.GetApp().keepGoing = False
        self.Destroy()
    def __del__( self ):
        pass


    
    
        
class MyApp(wx.App):
    def MainLoop111(self):
        # Create an event loop and make it active.  If you are
        # only going to temporarily have a nested event loop then
        # you should get a reference to the old one and set it as
        # the active event loop when you are done with this one...
        evtloop = wx.EventLoop()
        #print 'evtloop',evtloop
        #old = wx.EventLoop.GetActive()
        wx.EventLoop.SetActive(evtloop)

        # This outer loop determines when to exit the application,
        # for this example we let the main frame reset this flag
        # when it closes.
        while self.keepGoing:
            # At this point in the outer loop you could do
            # whatever you implemented your own MainLoop for.  It
            # should be quick and non-blocking, otherwise your GUI
            # will freeze.  
            # This inner loop will process any GUI events
            # until there are no more waiting.
            while evtloop.Pending():
                evtloop.Dispatch()

            # Send idle events to idle handlers.  You may want to
            # throttle this back a bit somehow so there is not too
            # much CPU time spent in the idle handlers.  For this
            # example, I'll just snooze a little...
            #gevent.sleep(0.1)
            self.ProcessIdle()
        self.Exit()
        #wx.EventLoop.Exit(evtloop)
        #wx.EventLoop.SetActive(old)

    def OnInit(self):
        frame = MyFrame1(None)
        frame.Show(True)
        self.SetTopWindow(frame)#optional
        #print 'frame:',frame
        self.keepGoing = True
        #print 'start_new_thread',svr_thd
        thread.start_new_thread(svr_thd,())
        #self.svr = testClient.myServer(('0.0.0.0',6011))
        #self.svr.run()
        
        return True

myEVT_ADD = wx.NewEventType()
EVT_ADD = wx.PyEventBinder(myEVT_ADD, 1)
myEVT_REMOVE = wx.NewEventType()
EVT_REMOVE = wx.PyEventBinder(myEVT_REMOVE, 1)
myEVT_UPDATE = wx.NewEventType()
EVT_UPDATE = wx.PyEventBinder(myEVT_UPDATE, 1)
class MyEvent(wx.PyCommandEvent):
    """Event to signal that a count value is ready"""
    def __init__(self, etype, eid, value=None):
        """Creates the event object"""
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._value = value

    def GetValue(self):
        """Returns the value from the event.
        @return: the value of this event

        """
        return self._value
    
def svr_thd():
    cfg = None
    with open('./cfg.yaml') as f:
        cfg = yaml.load(f)
    print cfg
    svr = guiserver(('0.0.0.0',cfg['server']['port']))
    svr.run()
    app = wx.GetApp()
    print 'apptopwindow:',app.GetTopWindow()
    while app.keepGoing:
        gevent.sleep(0.1)
    #print 'svr_end'
        #print 'svr_thd'
        
            
import thread
import gevent
import testClient
import yaml
class guiserver(testClient.myServer):
    def __init__(self,listener):
        super(guiserver,self).__init__(listener)
        
        self.frame = wx.GetApp().GetTopWindow()
        self.keepGoing = wx.GetApp().keepGoing
    
    def onconnected(self,address,uidstr):
        print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++guiserverconected:',address,uidstr
        #thread.start_new_thread(self.frame.addPanel,(uidstr,))
        wx.PostEvent(self.frame,MyEvent(myEVT_ADD,-1,uidstr))
        print '============================================================================================'
    def onclosed(self,address,uidstr): 
        print 'guiserverclosed:',address,uidstr
        wx.PostEvent(self.frame,MyEvent(myEVT_REMOVE,-1,uidstr))
    def posting_machine_state(self,uidstr,fj):
        #print dir(fj)
        #异步数据处理，需要拷贝数据
        if not self.keepGoing:
            return
        fjcp = FangJing_pb2.FangJing()
        fjcp.CopyFrom(fj)
        #print fjcp
        wx.PostEvent(self.frame,MyEvent(myEVT_UPDATE,-1,(uidstr,fjcp)))
        #print 'guiservermathcine_state'
        #print uidstr
        #print fj
        #self.frame.updatePanel2(uidstr,fj)
import FangJing_pb2        
import win32api
#import gevent.monkey
#gevent.monkey.patch_all(socket=True, dns=True, time=False, select=True, thread=False, os=True, ssl=True)
if __name__ == '__main__':
    global app 
    app = MyApp()
    app.MainLoop()
    