from log import logger

def mytest(a, b):
    if b == 0:
        logger.critical("除数不能0")
    return a / b


mytest(10, 0)
