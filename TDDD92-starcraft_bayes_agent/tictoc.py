import time


class TicToc:
    """
    Class to make the checking of how long times different parts of the program takes. Simply
    write tic() where you want to start the timer and toc() when you want to stop timer. Can handle
    multiple timers simultaneously by sending a key to tic and toc. Reset everything with reset()
    and a specific key by providing thus key
    """
    def __init__(self):
        self.logs = None
        self._time_start = {"main": 0.0}
        self.reset()

    def __repr__(self):
        """
        How the class should be printed, will print like a normal dictionary
        :return: Normal representation of a dictionary
        """
        return self.logs.__repr__()

    def __getitem__(self, item):
        """
        Getter to retrieve a single timer
        :param item: name of the log you want get
        :return: Timer of the provided name
        """
        return self.logs.get(item)

    def __iter__(self):
        """
        Iterator for the times
        :return: iterator for the times that are logged
        """
        return self.logs.items().__iter__()

    def tic(self, key="main"):
        """
        Start the timer for provided key
        :param key: Name of the timer, used to save start time in a dict, defaults to "main"
        :return: None
        """
        if key not in self.logs:
            self.logs[key] = 0.0
        self._time_start[key] = time.time()

    def toc(self, key="main"):
        """
        Saves the time for provided key. Can be used multiple times from the same tic() then it will do addition
        :param key: Name of the timer defaults to "main"
        :return: None
        """
        try:
            self.logs[key] += time.time() - self._time_start[key]

        except KeyError:
            "The provided key has not been initialized, need to run tic() before running toc()"

    def reset(self, key=None):
        """
        Reset the log for the given key if the key exists. Leave key empty to reset all logs
        :param key: what key you want to reset, defaults to None which will reset everything
        :return: None
        """
        if key is None:
            self.logs = {"main": 0.0}
        elif key in self.logs:
            self.logs[key] = 0.0
