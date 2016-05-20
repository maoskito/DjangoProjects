import ConfigParser

def config():
    con = ConfigParser.ConfigParser()
    path = "\start.ini"
    path = os.getcwd()+path
    f = open( path, 'r+')
    con.read( path)
    f.close()
    configs = {}
    configs["cloudValidateIP"] = con.get("Config","cloudValidateIP")
    configs["sendGap"] = con.get("Config","sendGap")
    configs["cloudDatabaseIP"] = con.get("Config","cloudDatabaseIP")
    configs["branchstoreNos"] = con.get("Config","branchstoreNos")
    configs["msgAmount"] = con.get("Config","msgAmount")
    
    return configs


set_1 = set([1,2,3,4])
set_2 = set([3,4,5,6])
print set_1>=set_2
