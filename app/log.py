import os
import logging
import logging.config

from config import HOME, LOG_DIR, LOG_FILE, ERROR_LOG_FILE, DEBUG_LOG_FILE


def setup_logging():
  if not os.path.exists(HOME):
    os.makedirs(HOME)

  log_dir = os.path.join(HOME, LOG_DIR)
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)

  logger = logging.getLogger('apiserver')
  logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(log_dir, LOG_FILE),
            'maxBytes': 10*1024*1024,
            'backupCount': 30,
            'encoding': 'utf8'
        },
        'error_file_handler': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(log_dir, ERROR_LOG_FILE),
            'maxBytes': 10*1024*1024,
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'debug_file_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(log_dir, DEBUG_LOG_FILE),
            'maxBytes': 20*1024*1024,
            'backupCount': 100,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'error_file_handler', 'debug_file_handler'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
  })
  __builtins__['logging'] = logger