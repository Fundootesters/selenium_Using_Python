import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info("This is Info message")
logging.debug("This is Debugg messgae")
logging.warning("Warnings messages")
logging.error("Error messages")
logging.critical("critical messages")