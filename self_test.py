# Redis实战学习

# ch5 使用Redis构建支持程序

import logging
import time

# 日志安全级别字典
SEVERITY = {
    logging.DEBUG: 'debug',
    logging.INFO: 'info',
    logging.WARNING: 'warning',
    logging.ERROR: 'error',
    logging.CRITICAL: 'critical',

}

# update()函数把字典(name,name)的键/值对更新到SEVERITY里
SEVERITY.update((name, name) for name in SEVERITY.values())


def log_recent(conn, name, message, severity=logging.INFO, pipe=None):
    severity = str(SEVERITY.get(severity, severity).lower())
    destination = 'recent:%s:%s' % (name, severity)
    message = time.asctime() + ' ' + message
    pipe = pipe or conn.pipeline()
    pipe.lpush(destination, message)
    pipe.ltrim(destination, 0, 99)  # 只包含最新的100条日志消息
    pipe.execute()
