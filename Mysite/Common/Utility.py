import ConfigParser

class myConfigParser(ConfigParser.ConfigParser):
    def __init__( self, filePath='start.ini'):
##        super( myConfigParser ,self).__init__()
        ConfigParser.ConfigParser.__init__( self)
        self.read( filePath)
    def get( self, section, option):
        try:
            return ConfigParser.ConfigParser.get( self, section, option)
        except ConfigParser.NoOptionError, e:
            print e
            return None
        except ConfigParser.NoSectionError, e:
            print e
            return None

    

c = myConfigParser()
print c.get( "section_one","option_1")
