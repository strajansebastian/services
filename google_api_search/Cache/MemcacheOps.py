import memcache

class Memcache():
	__host = None
	__port = None
	__connection = None

	def __init__(self, host, port):
		self.__host = host
		self.__port = port
		self.__connection = self.__connect()
	
	def __connect(self, debug = 0):
		return memcache.Client([self.__host + ':' + str(self.__port)], debug = debug)

	def set(self, key_name, key_value, expire):
		self.__connection.set(key_name, key_value, expire)

	def get(self, key_name):
		self.__connection.get(key_name)

	def delete(self, key_name):
		self.__connection.delete(key_name)

	def set_improved(self, key_name, key_value, expire, options):
		if options.get('key_name_remove_protocol'):
			key_name = key_name.ADD_REGEX
		if options.get('key_name_remove_hostname') == 1:
		
		self.set(key_name, key_value, expire)
