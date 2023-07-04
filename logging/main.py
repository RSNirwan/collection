import logging
from my_package import m1

logging.getLogger().setLevel(logging.DEBUG)
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(message)s"))
logger.addHandler(handler)

# basicConfig call will create a Streamhandler and add it to the root logger automatically
# next line does same as the lines above
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(name)s:%(message)s")

# formatting options
formatter = logging.Formatter(
    "%(name)-12s: %(levelname)-8s %(message)s - second logger"
)
handler2 = logging.StreamHandler()
handler2.setLevel(logging.DEBUG)
handler2.setFormatter(formatter)
logger.addHandler(handler2)

m1.f1()
m1.f2()
m1.f3()
