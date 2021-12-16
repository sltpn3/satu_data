from typing import Generator

from db.session import SessionLocal
import configparser

accepted_image = ['image/png', 'image/jpg', 'image/jpeg']


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()


def get_config():
    config = configparser.ConfigParser()
    config.read('app/config.conf')
    return config
