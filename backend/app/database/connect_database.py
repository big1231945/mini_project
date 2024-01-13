from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

db_host = 'localhost'
db_port = '3306'
db_user ='root'
db_password = ''
db_database = 'webhook_database'

engine = create_engine(
    url=f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_database}"
)
SessionLocal = Session(bind=engine,autocommit=False,)
Base = declarative_base()
