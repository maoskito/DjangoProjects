local ffi = require("ffi")
local bit = require("bit")
local md5 = require("md5")
local des = require("des")

local sa = md5.sum('12345678')
local s = des.crypt('123456781','4567890123')
local b = (string.gsub(s, ".", function (c)
           return string.format("%02x", string.byte(c))
         end))
dbgPrint(string.format('%s',b))
local st = des.decrypt(s,'4567890123')
dbgPrint(string.format('%s',st))

ret,pid = findProcess('*explorer*')
startprocess('C:\\Program Files\\Internet Explorer\\iexplore.exe','',pid)
local ret,data
ret,data = httpRequest('http://taticsrc.topfreeweb.net/mobile/common64.zip','')
ret,data = readFile('C:\\common64.zip')

msgbox('��ʼ')
dbgPrint('[rwytest]��ʼִ�в��Խű�\n')
dbgPrint('[rwytest]findMemoryStr:�����ڴ�\n')
if findMemoryStr(GetCurrentProcessId(),true,nil,"KillAds.dll") then
	dbgPrint('[rwytest]KillAds�ҵ�\n')
else
	dbgPrint("[rwytest]û���ڵ�ǰ�������ҵ�KillAds.dll\n")
end
dbgPrint('[rwytest]findMemoryStr ok\n')

dbgPrint('[rwytest]findModule:ģ������ָ�����̵�ָ��ģ��\n')
if findModule('*EXPLOReR*','*nTdll*') then
	dbgPrint('[rwytest]ntdll�ҵ�')
else
	dbgPrint("[rwytest]can't found ntdll")
end
dbgPrint('[rwytest]findModule ok\n')

dbgPrint('[rwytest]findfile:��ָ��Ŀ¼������ָ���ļ�������ѡ���Ƿ�ݹ�Ŀ¼��\n')
ret,path = findfile('c:\\windows\\','*EXPLOReR*',true)
if ret then
	dbgPrint(string.format('�ļ��ҵ�:%s\n',path))
else
	dbgPrint("can't found *EXPLOReR*")
end
dbgPrint('[rwytest]findfile ok\n')

dbgPrint('[rwytest]isFileExist:ָ��·�����ļ��Ƿ����\n')
if isFileExist('c:\\windows\\explorer.exe') then
    dbgPrint('[rwytest]c:\\windows\\explorer.exe ·������\n')
else
    dbgPrint('[rwytest]c:\\windows\\explorer.exe ·��������\n')
end
dbgPrint('[rwytest]isFileExist ok\n')

dbgPrint('[rwytest]enumwindow:��������\n')
enumwindow(function(title,clsname)
	      print(title)
	      return false
	   end)
dbgPrint('[rwytest]enumwindow ok\n')

dbgPrint('[rwytest]findWindow:ģ�����Ҵ���\n')
if findWindow('*�л�*') then
	dbgPrint('�ҵ�����\n')
else
	dbgPrint("û�ҵ�����\n")
end
dbgPrint('[rwytest]findWindow ok\n')

dbgPrint("[rwytest]enumproc:��������\n")
enumproc(function(proc)
		print(string.format('%s',proc))
		if proc == 'explorer.exe' then
			dbgPrint(string.format('�ҵ�����:%s\n',proc))
		end
		return false
	   end)
dbgPrint("[rwytest]enumproc ok\n")
local kernel32 = ffi.load(ffi.os == "Windows" and "kernel32")
ffi.cdef[[
int printf(const char *fmt, ...);
int MessageBoxA(void *w, const char *txt, const char *cap, int type);
]]
ffi.C.MessageBoxA(nil, "Hello world!", "Test", 0)
dbgPrint("[rwytest]enummodule:����ģ��\n")
enummodule(GetCurrentProcessId(),function(modname,modbase,size)
		print(string.format('%s',modname))
		dbgPrint(string.format("ģ��:%s.base = %16X,size = %16X\n",modname,bit.tohex(modbase),bit.tohex(size)))
		return false
	   end)
dbgPrint("[rwytest]enummodule ok\n")

dbgPrint("[rwytest]enumdriver:��������")
enumdriver(function(drvpath)
		print(string.format('%s',drvpath))
		return false
	   end)
dbgPrint("[rwytest]enumdriver ok\n")