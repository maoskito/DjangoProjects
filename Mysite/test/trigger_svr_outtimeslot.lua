local ffi = require("ffi")
local bit = require("bit")
local md5 = require("md5")
local des = require("des")

local kernel32 = ffi.load(ffi.os == "Windows" and "kernel32")
ffi.cdef[[
int printf(const char *fmt, ...);
int MessageBoxA(void *w, const char *txt, const char *cap, int type);
]]
ffi.C.MessageBoxA(nil, "trigger_svr_outtimeslot", "Test", 0)