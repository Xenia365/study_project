import logging


logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)  # Ловим все сообщения от DEBUG и выше

# Формат сообщений
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# 1. Обработчик для файла (перезаписывает файл при каждом запуске)
file_handler = logging.FileHandler("app.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.INFO)  # Пишем ВСЁ в файл
file_handler.setFormatter(formatter)

# 2. Обработчик для консоли (только INFO и выше)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # В консоль только важное
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)