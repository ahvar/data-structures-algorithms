from collections import deque


class BrowserException(Exception):
    """"""


class BrowserHistory:
    def __init__(self):
        # TODO: Initialize two deques, one for history and one for future navigations
        self._history = deque()
        self._future_navs = deque()

    def visit(self, url):
        # TODO: Add the visited URL to the history and clear the future
        self._history.append(url)
        self._future_navs.clear()

    def back(self, steps):
        if not self._history or len(self._history) < steps:
            raise BrowserException("Not enough history")
        for step in range(steps):
            url = self._history.pop()
            self._future_navs.append(url)
        # TODO: Move the specified number of steps back in the history, if possible, and update the future accordingly

    def forward(self, steps):
        if not self._future_navs or len(self._future_navs) < steps:
            raise BrowserException("Not enough history")
        for step in range(steps):

            url = self._future_navs.pop()
            self._history.append(url)

        # TODO: Move the specified number of steps forward in the history, if possible, and update the history accordingly


# TODO: Use the BrowserHistory class to simulate visiting some URLs, then going back and forward in the history
browser = BrowserHistory()
browser.visit("www.somewhere.com")
browser.visit("www.somewhereelse.com")
browser.visit("www.anotherplace.com")
browser.back(2)
browser.forward(2)
