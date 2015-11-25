Resystem common service package
===============================

This Python3-only package provides different classes and functions
which are used in various services, either proprietary or open,
such as [res-scheduler](https://github.com/AngryDevelopersLLC/res-scheduler).

It supposes [asyncio](http://asyncio.org/) environment.

* `argument_parser.py` provides scattered argparse support.
* `child_process_protocol.py` allows single parent - multiple
  children process operation, similar to classic web servers like
  Apache or (g)unicorn.
* `configuration.py` includes `Config` class and different helpers for
  building a nice JSON-based configuration system.
* `logger.py` supplies `Logger` class which simplifies and colorizes
  logging (other classes are supposed to inherit from it - screw
  the incapsulation).
* `systemd_watchdog.py` - [systemd](https://en.wikipedia.org/wiki/Systemd)
  watchdog wrapper (used in modern Debian/Ubuntu versions).
* `utils.py` - various random functions.

Released under New BSD license.
