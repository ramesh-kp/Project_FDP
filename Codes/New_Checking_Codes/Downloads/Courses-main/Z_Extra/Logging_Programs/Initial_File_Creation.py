import logging
logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', \
                    level = logging.DEBUG, filename = 'check.txt')
logging.debug("A Debug Logging Message")
logging.info("A Info Logging Message")
logging.warning("A Warning Logging Message")
logging.error("An Error Logging Message")
logging.critical("A Critical Logging Message")
