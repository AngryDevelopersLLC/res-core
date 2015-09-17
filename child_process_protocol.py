import asyncio
import sys
import os

from .logger import Logger


class ChildProcessProtocol(asyncio.SubprocessProtocol, Logger):
    def __init__(self, children, argv):
        super(ChildProcessProtocol, self).__init__()
        self._children = children
        self._argv = argv
        self.terminating = False

    @property
    def children(self):
        return self._children

    @property
    def transport(self):
        return self.children[self]

    def pipe_data_received(self, fd, data):
        os.write(fd, data)

    def process_exited(self):
        if self.terminating:
            self.info("Process %d exited with return code %d",
                      self.transport.get_pid(),
                      self.transport.get_returncode())
            return
        self.warning("Process %d exited with return code %d => restarting...",
                     self.transport.get_pid(), self.transport.get_returncode())
        del self.children[self]
        asyncio.async(self.restart())

    @asyncio.coroutine
    def restart(self):
        t, p = yield from asyncio.get_event_loop().subprocess_exec(
            lambda: ChildProcessProtocol(self.children, self._argv),
            sys.executable, *self._argv, stdin=None)
        self.children[p] = t
