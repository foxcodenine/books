from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.dialects.mysql import JSON

engine = create_engine('mysql+pymysql://F2udETTsO6:U7hQzPXXBW@remotemysql.com/F2udETTsO6',  pool_recycle=3600)

connection = engine.connect()
metadata = MetaData()

cookies = Table('cookies', metadata, 
    Column('cookie_id', Integer(),  primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unite_cost', Numeric(12,2))    
)

metadata.create_all(engine)