# 13. Logger
import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)


handler = TimedRotatingFileHandler(
    'my_log.log',
    when='midnight',
    interval=1,
    backupCount=7,
    encoding='utf-8'
)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


logger.addHandler(handler)


logger.info('This is a log message')
