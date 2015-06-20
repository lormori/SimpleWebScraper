from threading import Timer

class ScraperTimer(object):

    interval = 1
    function = None
    args = None
    _timer = None

    def __init__(self, interval, function, *args):
        self.interval = interval
        self.function = function ## the function to call with interval
        self.args = args
        self._timer = None
    
    def run(self):
        self.function(*self.args)
        self.start()

    def start(self):
        self._timer = Timer(self.interval, self.run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()
    