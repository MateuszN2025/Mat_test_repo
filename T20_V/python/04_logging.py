import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

logging.info("Program started")
logging.warning("Disk space is low")
logging.error("Device not connected")