import pandas as pd

from peewee import *

from db import DB



def df_from_knowledge() -> pd.DataFrame:

	db = DB.get_db()


	class BaseModel(Model):
		"""A base model that will use our Postgresql database"""
		class Meta:
			database = db


	class Knowledge(BaseModel):
		id = PrimaryKeyField()
		Number = CharField(max_length=1000)
		Question = CharField(max_length=1000)
		Products_name = CharField(max_length=1000)
		Products_Uids = CharField(max_length=10000)
		Ingreds = CharField(max_length=1000)
		Products = CharField(max_length=1000)
		Category = CharField(max_length=1000)
		rating = CharField(max_length=1000)
		cnt_items = CharField(max_length=1000)
		OrderPrice = CharField(max_length=1000)
		Combination = CharField(max_length=1000)
		HashCombination = CharField(max_length=1000)


	# получить список словарей
	sq = Knowledge.select().dicts()
	DB.close_db(db)
	df: pd.DataFrame = pd.DataFrame([i for i in sq])
	return df

df = df_from_knowledge()
print(type(df))
print(df.shape)

