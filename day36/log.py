import logging

# logging.basicConfig(filename='log.txt', level=logging.DEBUG,format='%(asctime)s %(message)s')
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler(filename='log.txt')
fh.setLevel(logging.WARNING)


class stringFilter(logging.Filter):
    def filter(self, record):
        if record.msg.find("abc") == -1:
            return True
        return False


form=logging.Formatter("%(asctime)s -- %(name)s -- %(message)s")

sh.setFormatter(form)
fh.setFormatter(form)

fh.addFilter(stringFilter())

logger.addHandler(sh)
logger.addHandler(fh)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
logger.warning("abcdef")