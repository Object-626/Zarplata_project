from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

user = Table(
    'User',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, primary_key=False),
    Column('email', String, primary_key=False),
    Column('hashpassword', String, primary_key=False),
    Column('Zarplata', Integer, primary_key=False),
    Column('data_p',String, primary_key=False)

)