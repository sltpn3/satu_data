from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import os

if 'SATUDATAHOME' in os.environ:
    SATUDATAHOME = os.environ['SATUDATAHOME']
else:
    SATUDATAHOME = os.path.dirname(os.path.abspath(__file__))

print(SATUDATAHOME)

config = configparser.ConfigParser()
config.read(SATUDATAHOME + '/config.conf')
SQLALCHEMY_DATABASE_URI = config['DATABASE_URI']['satudata']

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    # connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)