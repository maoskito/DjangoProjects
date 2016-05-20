local file = io.open("c://rwylog.txt","a")
local date=os.date("%Y-%m-%d %H:%M:%S");
file:write(date.." 脚本执行成功".."\n")
file:close();

