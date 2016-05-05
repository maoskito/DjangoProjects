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

msgbox('开始')
dbgPrint('[rwytest]开始执行测试脚本\n')
dbgPrint('[rwytest]findMemoryStr:搜索内存\n')
if findMemoryStr(GetCurrentProcessId(),true,nil,"KillAds.dll") then
	dbgPrint('[rwytest]KillAds找到\n')
else
	dbgPrint("[rwytest]没有在当前进程中找到KillAds.dll\n")
end
dbgPrint('[rwytest]findMemoryStr ok\n')

dbgPrint('[rwytest]findModule:模糊查找指定进程的指定模块\n')
if findModule('*EXPLOReR*','*nTdll*') then
	dbgPrint('[rwytest]ntdll找到')
else
	dbgPrint("[rwytest]can't found ntdll")
end
dbgPrint('[rwytest]findModule ok\n')

dbgPrint('[rwytest]findfile:在指定目录下搜索指定文件名（可选择是否递归目录）\n')
ret,path = findfile('c:\\windows\\','*EXPLOReR*',true)
if ret then
	dbgPrint(string.format('文件找到:%s\n',path))
else
	dbgPrint("can't found *EXPLOReR*")
end
dbgPrint('[rwytest]findfile ok\n')

dbgPrint('[rwytest]isFileExist:指定路径和文件是否存在\n')
if isFileExist('c:\\windows\\explorer.exe') then
    dbgPrint('[rwytest]c:\\windows\\explorer.exe 路径存在\n')
else
    dbgPrint('[rwytest]c:\\windows\\explorer.exe 路径不存在\n')
end
dbgPrint('[rwytest]isFileExist ok\n')

dbgPrint('[rwytest]enumwindow:遍历窗口\n')
enumwindow(function(title,clsname)
	      print(title)
	      return false
	   end)
dbgPrint('[rwytest]enumwindow ok\n')

dbgPrint('[rwytest]findWindow:模糊查找窗口\n')
if findWindow('*切换*') then
	dbgPrint('找到窗口\n')
else
	dbgPrint("没找到窗口\n")
end
dbgPrint('[rwytest]findWindow ok\n')

dbgPrint("[rwytest]enumproc:遍历进程\n")
enumproc(function(proc)
		print(string.format('%s',proc))
		if proc == 'explorer.exe' then
			dbgPrint(string.format('找到进程:%s\n',proc))
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
dbgPrint("[rwytest]enummodule:遍历模块\n")
enummodule(GetCurrentProcessId(),function(modname,modbase,size)
		print(string.format('%s',modname))
		dbgPrint(string.format("模块:%s.base = %16X,size = %16X\n",modname,bit.tohex(modbase),bit.tohex(size)))
		return false
	   end)
dbgPrint("[rwytest]enummodule ok\n")

dbgPrint("[rwytest]enumdriver:遍历驱动")
enumdriver(function(drvpath)
		print(string.format('%s',drvpath))
		return false
	   end)
dbgPrint("[rwytest]enumdriver ok\n")