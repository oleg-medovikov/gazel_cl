from starlette.config import Config

config = Config("config.cfg")

DATABASE_URL=config("DATABASE_URL", cast=str)
SALT=config("SALT", cast=str)
DEFAULT_USERNAME=config("DEFAULT_USERNAME", cast=str)

USER_FIRST_NAME = "test"
USER_TOKEN = ""
USER_POSITION = ""


FONT_GRID_SIZE = config("FONT_GRID_SIZE", cast=str)
