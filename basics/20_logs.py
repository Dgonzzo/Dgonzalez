import logging

logging.basicConfig(level=logging.DEBUG)


logging.debug('Debugging message') # Lowest level of diagnosis
logging.info('Info message') # Level of information
logging.warning('Warning message') # Level where it could be a problem
logging.error('Error message') # There is an error on the app
logging.critical('Critical message') # Important error