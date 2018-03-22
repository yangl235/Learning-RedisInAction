#Redis实战学习

#ch5 使用Redis构建支持程序

import logging

#日志安全级别字典
SEVERITY = {
        logging.DEBUG: 'debug',
        logging.INFO: 'info',
        logging.WARNING: 'warning',
        logging.ERROR: 'error',
        logging.CRITICAL: 'critical',

}

#update()函数把字典(name,name)的键/值对更新到SEVERITY里
SEVERITY.update((name, name) for name in SEVERITY.values())




