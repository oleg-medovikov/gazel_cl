from starlette.config import Config



config = Config("config.cfg")


DATABASE_URL=config("DATABASE_URL", cast=str, default='')

SALT=config("SALT", cast=str, default='')

DEFAULT_USERNAME=config("DEFAULT_USERNAME", cast=str, default='')

FONT_GRID_SIZE = config("FONT_GRID_SIZE", cast=str, default='')
