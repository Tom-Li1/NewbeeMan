TIMEOUT /T 7

set msg="An error has occured. There is a possibility that your conputer is infected with virus."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"System Error")(window.close)
TIMEOUT /T 3

set msg="You don't have access to make the required system configuration modifications. \nProcess terminated"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Users")(window.close)
TIMEOUT /T 7

set msg="���ϵͳ���ִ��󣺴��豸���ƴ��ڰ�ȫ�����⡣�����������Ȼ���ڣ�����ϵͳ����Ա��ϵ��\n\n���֤״̬[1.1.98]"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"���ϵͳ")(window.close)
TIMEOUT /T 4

set msg="Unable to find local data files, please reinstall."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Missing File Error")(window.close)
TIMEOUT /T 8

set msg="'0xc00255f' ָ�����õ� '0x023c6c20' �ڴ治��Ϊ 'written' ��\n���ȷ������ֹ����"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"SAS Window: winlogon.exe - Ӧ�ó������")(window.close)
TIMEOUT /T 4

set msg="Windows �޷����ӵ���ӡ��\n����ʧ�ܣ�����Ϊ 0x000003e3"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"��Ӵ�ӡ��")(window.close)
TIMEOUT /T 3

set msg="Ӧ�ó������쳣 Unknow software exception (0xc0000417)\nλ��Ϊ 0x004096d6\n\nҪ��ֹ��������ȷ����"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"Ӧ�ó������")(window.close)
TIMEOUT /T 8

set msg="An error applying attribures to the file: C:\Windows\security\database\edb.chk\n\nThe requested operation delegation to be enabled on the machine."
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),48,"Error Applying Attributes")(window.close)
TIMEOUT /T 3

set msg="��⵽ע��������޸ģ��ָ��ɹ�"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),64,"Windows - ע�����ϻָ�")(window.close)
TIMEOUT /T 4

set msg="Ӧ�ó�������쳣��λ�õ�����쳣 (0xc0000409)"
mshta vbscript:msgbox(Replace(%msg%,"\n",vbCrLf),16,"winlogon.exe - Ӧ�ó������")(window.close)
