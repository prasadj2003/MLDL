from logger import logging

def add(a, b):
    logging.debug("The addidtion operation is taking place")
    return a+b

logging.debug("this addition function is called")
add(10, 15)