import logging.config
import sys
from myscrapper import MyScrapper

logging.config.fileConfig('logging.conf', defaults={'logfilename': 'logfile.log'}, disable_existing_loggers=False)
logger = logging.getLogger('customLogger')

name = sys.argv[1]
url = sys.argv[2]
obj = MyScrapper(name, url)
