import logging

logger = logging.getLogger("print_text")
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

ch.setFormatter(formatter)
logger.addHandler(ch)
