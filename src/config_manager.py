import ConfigParser

class Callable:

    def __init__(self, anycallable):
        self.__call__ = anycallable

class ConfigManager:
	
	_init = False
	_config = False
	
	def init(filename):
		ConfigManager._init = True
		ConfigManager._config = ConfigParser.ConfigParser()
		ConfigManager._config.read(filename)
		
		#for section in config.sections():
		#	print section
		#	for option in config.options(section):
		#		print " ", option, "=", config.get(section, option)

	def get(section, option):
		if ConfigManager._init == False:
			ConfigManager.init("client.conf")			
		return ConfigManager._config.get(section, option)

	init = Callable(init)
	get = Callable(get)


ConfigManager.init("client.conf")
