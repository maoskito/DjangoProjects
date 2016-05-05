local ffi = require('ffi')

local kernel32 = ffi.load(ffi.os == "Windows" and "kernel32")
ffi.cdef[[
int printf(const char *fmt, ...);
int MessageBoxA(void *w, const char *txt, const char *cap, int type);
]]
ffi.C.MessageBoxA(nil, "Hello rwynet!", "Test", 0)