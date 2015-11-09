import pymongo

class DbMongo():
	__connection = None
	__database = None

	def __init__(self, host, port, database):
		self.__connection = self.__connect(host, port)
		self.__database = self.__get_db(self.__connection, database)

	def __connect(self, host, port):
		print("Done")
		if self.__connection == None:
			return pymongo.MongoClient(host, port)
		return self.__connection

	def __get_db(self, connection, db):
		return connection[db]

	def get_collection(self, db, collection):
		return db[collection]

	def add(self, collection, json):
		col = self.get_collection(self.__database, collection)
		print("ADD")
		doc_id = col.insert_one({"data": "test1", "v2": "ts v34"})
		print("ADD DONE")
		return doc_id


