from typing import Optional
from peewee import PostgresqlDatabase

class DB:
	@staticmethod
	def get_db() -> Optional[PostgresqlDatabase]:
		try:
			# пытаемся подключиться к базе данных
			pg_db = PostgresqlDatabase('db1', user='user1', password='12345678',
									host='rc1b-wk8y07bcypyswmiv.mdb.yandexcloud.net', port=6432)
			pg_db.connect()
			return pg_db
		except Exception as err:
			# в случае сбоя подключения будет выведено сообщение в STDOUT
			print('Can`t establish connection to database: {}'.format(err))
			return None
	@staticmethod
	def close_db(pg_db):
		pg_db.close()