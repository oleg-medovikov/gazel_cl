from starlette.config import Config
from pathlib import Path

# Путь для файла конфигураций
config = Config("config.cfg")

# Путь для рабочей директории 
ROOT = Path(Path.home(), 'Documents', 'WORKSPACE')

# Адрес базы данных
DATABASE_URL=config("DATABASE_URL", cast=str, default='')

# Соль для кеширования пароля
SALT=config("SALT", cast=str, default='')

# Пользователь по умолчанию
DEFAULT_USERNAME=config("DEFAULT_USERNAME", cast=str, default='')

# Размер шрифта текста 
FONT_TEXT_SIZE = config("FONT_TEXT_SIZE", cast=str, default='0.5cm')

# Размер шрифта в окнах ввода 
FONT_INPUT_SIZE = config("FONT_INPUT_SIZE", cast=str, default='0.5cm')

# Размер шрифта в списках
FONT_GRID_SIZE = config("FONT_GRID_SIZE", cast=str, default='0.5cm')

# Размер большого окна
BIG_WINDOW = (
    config("BIG_WINDOW_X", cast=int, default = 600 ),
    config("BIG_WINDOW_Y", cast=int, default = 700 )
    )

# Размер малого окна
SMALL_WINDOW = (
    config("SMALL_WINDOW_X", cast=int, default = 375 ),
    config("SMALL_WINDOW_Y", cast=int, default = 700 )
        )

