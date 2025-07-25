from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine,Column,String,Integer


engine = create_engine("postgresql://postgres:manuel@localhost/sajayins")
Base = declarative_base()
sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

