import gevent.monkey

gevent.monkey.patch_all(thread=False)

import logging

from crawler import Crawler
from crawler.config import default_config

if __name__ == '__main__':
    entry_url = 'https://learn.lianglianglee.com'
    config = {
        ## 目标网站主页
        'main_url': entry_url,
        ## 抓取深度, 从当前页面算起, 1表示只抓当前页, 0表示无限制
        'max_depth': 2,
        'max_retry_times': 50,
        'headers': {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        },
        ## 按选择器删除部分内容
        'selectors_to_remove': [
            'div.book-sidebar'
        ],
        'access_too_frequent_texts': [
            'You are being rate limited'
        ],
        'outsite_asset': False,
        'no_js': True,
        'no_css': True,
        'no_images': False,
        'no_fonts': True,
        'no_audio': True,
        'no_video': True,
        'logging_config': {
            'level': logging.DEBUG,
            ## %(name)s表示模块路径(其实是__name__的值)
            'format': '%(asctime)s %(levelname)-7s %(name)s - %(filename)s:%(lineno)d %(message)s',
        }
    }
    config = dict(default_config, **config)

    logging.basicConfig(**config['logging_config'])
    ## logger.setLevel(logging.DEBUG)
    try:
        c = Crawler(config)
        c.start()
    except KeyboardInterrupt:
        c.stop()
