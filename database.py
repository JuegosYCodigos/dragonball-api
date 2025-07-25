import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://db_dragonball_user:f1KpFbbOFTQUTtYBs0ifw2uwdIA89qCS@dpg-d21g0qvgi27c73dsekg0-a.oregon-postgres.render.com/db_dragonball")

#DATABASE_URL = os.getenv("postgresql://db_dragonball_user:f1KpFbbOFTQUTtYBs0ifw2uwdIA89qCS@dpg-d21g0qvgi27c73dsekg0-a.oregon-postgres.render.com/db_dragonball") 
#DATABASE_URL = "postgresql://db_dragonball_user:f1KpFbbOFTQUTtYBs0ifw2uwdIA89qCS@dpg-d21g0qvgi27c73dsekg0-a.oregon-postgres.render.com/db_dragonball"

engine = create_engine(DATABASE_URL)

Base = declarative_base()
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
