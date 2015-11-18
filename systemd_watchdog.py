# RES Service Package
# Copyright © 2015 InvestGroup, LLC


import asyncio
import logging


def install_watchdog(interval, loop=None):
    assert isinstance(interval, (int, float)) and interval > 0
    logger = logging.getLogger("systemd-watchdog")
    try:
        from systemd.daemon import notify as sd_notify
    except ImportError:
        logger.warning("Failed to import systemd => watchdog is disabled")
        return
    if loop is None:
        loop = asyncio.get_event_loop()

    def notify():
        sd_notify("WATCHDOG=1")
        loop.call_later(interval, notify)

    notify()
    logger.info("Installed watchdog notification once per %s sec" % interval)
