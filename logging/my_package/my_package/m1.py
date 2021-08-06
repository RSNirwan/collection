import logging

log = logging.getLogger(__name__)


def f1():
    log.info('f1 called')

def f2():
    log.debug('f2 called')

def f3():
    log.warning('f3 called')
