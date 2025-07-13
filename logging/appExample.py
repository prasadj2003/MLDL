import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("appExample.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithematicApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def sub(a,b):
    result = a-b
    logger.debug(f"substracting {a}-{b} = {result}")
    return result

def mult(a,b):
    result = a*b
    logger.debug(f"Multiplying {a}*{b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None


add(5,51.6)
sub(74.56, 89.36)
mult(23.58, 45.89)
divide(4,0)
divide(45.29, 89.71)
