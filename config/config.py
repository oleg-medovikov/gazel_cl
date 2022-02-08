from starlette.config import Config

config = Config("config.cfg")

DATABASE_URL=config("DATABASE_URL", cast=str)
SALT=config("SALT", cast=str)


USER_FIRST_NAME = "test"
USER_TOKEN = ""
USER_POSITION = ""
