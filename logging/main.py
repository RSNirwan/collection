import logging
from my_package import m1

# basicConfig call will create a Streamhandler and add it to the root logger automatically
#logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(message)s"))
logger.addHandler(handler)

m1.f1()
m1.f2()
m1.f3()
