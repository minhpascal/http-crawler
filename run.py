#! /usr/bin/env python
# -*- coding: utf-8 -*-

from manager import Manager

API_LOGIN = ""
API_PASSWD = ""

manager = Manager()


@manager.command
def fetch(limit=100, retreive_all=False):
    "Crawl the feeds with the client crawler."
    from http_crawler import CrawlerScheduler
    scheduler = CrawlerScheduler(API_LOGIN, API_PASSWD)
    scheduler.run(limit=limit, retreive_all=retreive_all)
    scheduler.wait()


if __name__ == '__main__':
    manager.main()
