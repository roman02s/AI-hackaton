import pandas as pd

from peewee import *

from src.db import DB



db = DB.get_db()

# Index(['Number', 'Question', 'Products_name', 'Products_Uids', 'Ingreds',
        # 'Products', 'Category', 'rating', 'cnt_items', 'OrderPrice',
        # 'Unnamed: 10', 'Combination', 'HashCombination'],

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

if not db:
	print("Can`t connect to database")
	exit(1)

if Knowledge.table_exists():
	Knowledge.drop_table()
	print("drop table Knowledge")
Knowledge.create_table()
print("create table Knowledge")
# insert data
df = pd.read_csv('Knowledge_Base.csv')
df = df.drop(['Unnamed: 10'], axis=1)
print(type(df.to_dict('records')), type(df.to_dict('records')[0]))
print(df.to_dict('records')[0])
# df.columns to list

print(df.columns)
print(df.to_dict('records')[0])
# вставить данные df в Knowledge
with db.atomic():
	Knowledge.insert_many(df.to_dict('records'), fields=list(df.columns)).execute()

# вывести количество строк в таблице
print("In table Postgresql Knowledge: ", Knowledge.select().count())
print("In dataFrame: ", len(df))

DB.close_db(db)
