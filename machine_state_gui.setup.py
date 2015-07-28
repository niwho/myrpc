#coding=gbk

import py2exe

from distutils.core import setup
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "1.0.0.0"
        self.company_name = u"niwho"
        self.copyright = "Copyright (c) 2015 niwho."
        self.name = "nw"

target = Target(
    description = u"example",
    script = "machine_state_gui.py",
    icon_resources = [(1, r'PyCrust.ico')],
    dest_base = "machine_state",
    ######uac_execution_info="requireAdministrator"##这句没效果
    #uac_info= "requireAdministrator",##这句有用
    )
    

options = {"py2exe": 
{

"dist_dir":"./pub", 
"compressed":1, 
"optimize": 2, 
"bundle_files":1
 ,"dll_excludes": [ "MSVCP90.dll", "mswsock.dll", "powrprof.dll","w9xpopen.exe",
                  #'msvcr71.dll', "IPHLPAPI.DLL", "NSI.dll",  "WINNSI.DLL",  "WTSAPI32.dll",'psapi.dll',
                  'API-MS-Win-Core-ErrorHandling-L1-1-0.dll',
                  'API-MS-Win-Core-File-L1-1-0.dll',
                  'API-MS-Win-Core-IO-L1-1-0.dll',
                  'API-MS-Win-Core-LibraryLoader-L1-1-0.dll',
                  'API-MS-Win-Core-Handle-L1-1-0.dll',
                  'API-MS-Win-Core-Heap-L1-1-0.dll',
                  'API-MS-Win-Core-Interlocked-L1-1-0.dll',
                  'API-MS-Win-Core-Localization-L1-1-0.dll',
                  'API-MS-Win-Core-Memory-L1-1-0.dll',
                  'API-MS-Win-Core-Misc-L1-1-0.dll',
                  'API-MS-Win-Core-ProcessThreads-L1-1-0.dll',
                  'API-MS-Win-Core-Profile-L1-1-0.dll',
                  'API-MS-Win-Core-String-L1-1-0.dll',
                  'API-MS-Win-Core-Synch-L1-1-0.dll',
                  'API-MS-Win-Core-SysInfo-L1-1-0.dll',
                  'API-MS-Win-Core-ErrorHandling-L1-1-0.dll'
                  ]
#,"includes":["PCCUserppyy"]
}
}
setup(
      options = options, 
      #data_files = Mydata_files,
      zipfile = None ,
      console = [target]
      )
