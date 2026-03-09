import sqlalchemy as db

print(db.__version__)

engine= db.create_engine('sqlite:///data.db')
conn=engine.connect()
metadata=db.MetaData()
teams=db.table("teams",metadata, 
               db.column('teams_id',primary_key=True))
engine=create_engine('sqlite:///data.db')