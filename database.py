from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRECT_FILE = os.path.join(BASE_DIR, "secrets.json")
secrects = json.loads(open(SECRECT_FILE).read())
DB = secrects["DB"]
DB_URL = (
    f"mysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['dbname']}"
)
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
