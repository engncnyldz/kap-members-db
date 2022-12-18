from pydantic import BaseSettings
import logging
from logging.handlers import TimedRotatingFileHandler
from enum import IntEnum

class LogLevelEnum(IntEnum):
    info = logging.INFO
    debug = logging.DEBUG
    warn = logging.WARN
    error = logging.ERROR


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    database_username: str 
    database_password: str 
    log_level: LogLevelEnum = LogLevelEnum.info

    class Config:
        env_file = ".env"
        
settings = Settings()

logger = logging.getLogger("kap_members_db_logger")

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = TimedRotatingFileHandler("./logs/app.log", when="midnight",backupCount=30)
file_handler.setFormatter(formatter)
file_handler.setLevel(settings.log_level)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.ERROR)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

