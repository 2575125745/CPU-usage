# -*- coding: utf-8 -*-
# 初始化logger
import logging
import logging.handlers
import sys

import time


class logger:
    log = logging.getLogger()
    # 日志格式，可以根据需要设置
    fmt = logging.Formatter('[%(asctime)s][%(filename)s][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    logname = './log.log'
    # 日志输出到文件，日志名称，大小，保存个数
    handle1 = logging.handlers.RotatingFileHandler(logname, maxBytes=1024*1024*8, backupCount=3)
    handle1.setFormatter(fmt)
    # 同时输出到屏幕，便于实施观察
    handle2 = logging.StreamHandler(stream=sys.stdout)
    handle2.setFormatter(fmt)
    log.addHandler(handle1)
    log.addHandler(handle2)

    # 设置日志基本，这里设置为INFO，表示只有INFO级别及以上的会打印
    log.setLevel(logging.INFO)

    # 日志接口，用户只需调用这里的接口即可，这里只定位了INFO, WARNING, ERROR三个级别的日志，可根据需要定义更多接口
    @classmethod
    def info(cls, msg):
        cls.log.info(msg)
        return

    @classmethod
    def warning(cls, msg):
        cls.log.warning(msg)
        return

    @classmethod
    def error(cls, msg):
        cls.log.error(msg)
        return


