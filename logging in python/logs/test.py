
from loger import logging 
def add(a,b):
    logging.debug("Adding two numbers")
    return a+b


logging.debug("the addition function is called")
add(10,15)