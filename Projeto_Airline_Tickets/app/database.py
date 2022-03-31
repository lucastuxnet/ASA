import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, insert, delete
from models import Base
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
                                         
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.query = db_session.query_property()

def init_db():    
    import models
    Base.metadata.create_all(bind=engine)
